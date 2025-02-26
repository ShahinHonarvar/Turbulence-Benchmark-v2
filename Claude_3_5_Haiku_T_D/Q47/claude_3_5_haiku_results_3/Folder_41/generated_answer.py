def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[1:8].lower()
    for start in range(len(substring)):
        for end in range(start + 2, len(substring) + 1):
            if end - start in (3, 4):
                substr = substring[start:end]
                if substr == substr[::-1] and substr.isalpha():
                    palindromes.add(substr)
    return palindromes