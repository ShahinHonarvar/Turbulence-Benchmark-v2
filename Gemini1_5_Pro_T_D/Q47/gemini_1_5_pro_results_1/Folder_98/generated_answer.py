def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, min(i + 81, len(s) + 1)):
            substring = s[i:j]
            if len(substring) >= 5 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes