def palindromes_between_indices(s):
    substring = s[1:4]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            sub_str = substring[i:j + 1]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str.lower())
    return palindromes