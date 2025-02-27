def all_even_ints_inclusive(int_list):
    ans = []
    for i in range(64, 67):
        if int_list[i] % 2 == 0:
            ans.append(int_list[i])
    return ans