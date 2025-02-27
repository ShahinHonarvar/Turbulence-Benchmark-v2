def palindromes_between_indices(s):
    chars = s[4:8]
    chars = ''.join([c for c in chars if c.isalpha()])
    chars = chars.lower()
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            substring = chars[i:j + 1]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring[::-1])
    return palindromes