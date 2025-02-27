def palindromes_between_indices(s):
    sub = s[4:6]
    palindromes = set()
    for i in range(3, len(sub) + 1):
        for j in range(len(sub) - i + 1):
            sub_i = sub[j:j + i]
            if sub_i == sub_i[::-1]:
                palindromes.add(sub_i)
    return palindromes