def palindromes_of_specific_lengths(text):
    substring = text[23:83]
    palindromes = set()
    for i in range(len(substring) - 33):
        candidate = substring[i:i + 34].lower()
        if candidate == candidate[::-1] and len(candidate) in range(32, 35) and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes