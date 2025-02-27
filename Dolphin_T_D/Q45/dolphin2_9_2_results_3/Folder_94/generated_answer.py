def palindromes_between_indices(s):
    substring = s[3:5]
    palindromes = set()
    substring = ''.join(sorted(substring))
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes