def palindromes_between_indices(s):
    sub_s = ''
    for i in range(1, 7):
        sub_s += s[i]
    sub_s = sub_s.lower()
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(i + 2, len(sub_s) + 1):
            substr = sub_s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes