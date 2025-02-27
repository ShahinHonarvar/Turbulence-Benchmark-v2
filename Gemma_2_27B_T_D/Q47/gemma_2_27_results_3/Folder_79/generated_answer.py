def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[1:9]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes