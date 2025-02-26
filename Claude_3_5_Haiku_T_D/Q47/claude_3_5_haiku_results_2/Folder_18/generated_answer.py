def palindromes_of_specific_lengths(s):
    palindromes = set()
    for start in range(11, 84):
        for length in range(13, 67):
            if start + length > len(s):
                break
            substring = s[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes