def palindromes_between_indices(s):
    s = s[4:8].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes