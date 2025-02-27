def all_even_ints_inclusive(ls):
    ans = []
    for i in range(30, 201):
        try:
            temp = ls[i]
            if temp % 2 == 0:
                ans.append(temp)
        except IndexError:
            pass
    return ans