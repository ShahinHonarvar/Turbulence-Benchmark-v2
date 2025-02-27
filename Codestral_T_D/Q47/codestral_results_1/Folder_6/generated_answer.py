def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    palindromes = set()
    for length in range(40, 48):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes