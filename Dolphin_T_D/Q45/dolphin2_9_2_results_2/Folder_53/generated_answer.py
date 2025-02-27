def palindromes_between_indices(s):
    sub_s = s[4:9]
    sub_s = ''.join([c for c in sub_s if c.isalpha()])
    sub_s = sub_s.lower()
    palindromes = set()
    for length in range(6, len(sub_s) + 1):
        for start in range(len(sub_s) - length + 1):
            substring = sub_s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes