def palindromes_between_indices(str_):
    ans = set()
    for i in range(5, 7):
        str_list = list(str_)
        for comb in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat == 7 - i):
            for j in range(i):
                str_list[j + 5] = comb[j]
            str_list[i + 5] = comb[i]
            ans.add(''.join(str_list))
    return ans