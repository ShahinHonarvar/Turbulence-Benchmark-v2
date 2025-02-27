def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes