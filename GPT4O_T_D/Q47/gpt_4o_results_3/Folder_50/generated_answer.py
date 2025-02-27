def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s[36:93])).lower()
    palindromes = set()
    for length in range(10, 36):
        for start in range(len(s) - length + 1):
            snippet = s[start:start + length]
            if snippet == snippet[::-1]:
                palindromes.add(snippet)
    return palindromes