def sum_even_ints_inclusive(lst):
    ans = 0
    for i in range(56, 99):
        if lst[i] % 2 == 0:
            ans += lst[i]
    return ans