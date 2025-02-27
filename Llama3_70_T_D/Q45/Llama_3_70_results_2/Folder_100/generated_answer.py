def palindromes_between_indices(s):
    s = s[:6].lower()
    palindromes = set()
    for length in range(6, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            substr = ''.join(filter(str.isalpha, substr))
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes