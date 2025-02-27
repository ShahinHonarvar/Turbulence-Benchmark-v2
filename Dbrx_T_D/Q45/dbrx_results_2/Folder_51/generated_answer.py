def palindromes_between_indices(s):
    palindromes = set()
    for i in range(3, 6):
        for j in range(i, 6 - i + 2):
            sub_s = s[i:j].lower()
            if sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes