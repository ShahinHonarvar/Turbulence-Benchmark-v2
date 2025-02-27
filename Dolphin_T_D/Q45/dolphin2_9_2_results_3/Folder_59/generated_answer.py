def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub_s = s[8:10]
    sub_s = ''.join(filter(str.isalpha, sub_s))
    sub_s = sub_s.lower()
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(i + 2, len(sub_s) + 1):
            sub_sub_s = sub_s[i:j]
            if sub_sub_s == sub_sub_s[::-1]:
                palindromes.add(sub_sub_s)
    return palindromes