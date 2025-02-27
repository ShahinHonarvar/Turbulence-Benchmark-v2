def palindromes_between_indices(s):
    substr = ''.join((c for c in s[1:6] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 3, len(substr) + 1):
            candidate = substr[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes