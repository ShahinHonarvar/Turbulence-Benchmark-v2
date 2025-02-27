def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[2:4].lower()))
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes