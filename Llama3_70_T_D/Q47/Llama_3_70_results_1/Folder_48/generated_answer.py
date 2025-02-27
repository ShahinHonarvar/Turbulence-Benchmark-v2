def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    palindromes = set()
    for length in range(104, 121):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes