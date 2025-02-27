def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[31:92]
    for i in range(len(substring) - 52):
        candidate = substring[i:i + 53].lower()
        if candidate == candidate[::-1] and len(candidate) in range(50, 54) and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes