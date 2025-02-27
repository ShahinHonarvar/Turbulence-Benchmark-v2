def palindromes_between_indices(s):
    substring = s[5:7]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            if substring[i:j].lower() == substring[i:j].lower()[::-1] and len(substring[i:j]) >= 3:
                palindromes.add(substring[i:j])
    return palindromes