def palindromes_between_indices(s):
    substring = s[4:7]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes