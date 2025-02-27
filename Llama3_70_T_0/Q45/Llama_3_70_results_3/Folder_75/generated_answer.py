def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) >= 3:
                palindromes.add(substr)
    return palindromes