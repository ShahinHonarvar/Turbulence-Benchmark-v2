def all_odd_ints_inclusive(lin):
    ans = []
    for i in range(661, 925):
        if i % 2 == 1:
            ans.append(lin[i])
    if ans == []:
        ans = []
    return ans