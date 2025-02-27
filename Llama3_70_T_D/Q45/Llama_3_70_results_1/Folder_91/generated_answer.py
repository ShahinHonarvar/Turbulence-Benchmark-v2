def palindromes_between_indices(s):
    s = s[2:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes