def find_subset_of_length_n(s):
    if len(s) < 45:
        return 0
    ans = 0
    for i in range(len(s)):
        if s[i] > 45:
            continue
        tmp = s.copy()
        tmp.remove(s[i])
        ans += find_subset_of_length_n(tmp)
    if 45 in s:
        ans += 1
    return ans