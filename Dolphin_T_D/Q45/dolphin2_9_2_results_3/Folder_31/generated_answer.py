def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1].lower()
    if len(s) <= 8:
        return set()
    sub_s = ''
    open_set = ''
    for i in range(1, 9):
        sub_s += s[i]
    for perm in permutations(sub_s):
        for i in range(5, 8):
            pal_sub_s = ''
            for j in range(i):
                pal_sub_s += perm[j]
            if is_palindrome(pal_sub_s):
                open_set += pal_sub_s
    if len(open_set) == 0:
        return set()
    pal_set = set()
    for i in range(1, 8):
        sub_pal_set = set()
        for perm in permutations(open_set[i]):
            sub_pal_set.add(perm + perm[::-1])
        for ii in sub_pal_set:
            if is_palindrome(ii):
                if len(ii) >= 6:
                    pal_set.add(ii)
    return pal_set