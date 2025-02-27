def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    s = ''.join(sorted(s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes