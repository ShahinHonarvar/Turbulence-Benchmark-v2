def palindromes_between_indices(s):
    substring = ''.join((c for c in s[:4] if c.isalpha())).lower()
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(i + 3, length + 1):
            candidate = substring[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes