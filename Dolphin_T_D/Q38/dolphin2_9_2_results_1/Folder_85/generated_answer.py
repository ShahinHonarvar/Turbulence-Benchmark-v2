def find_subset_of_length_n(s):
    if len(s) < 23:
        return 0
    ans = 0
    for i in s:
        rest = s.copy()
        rest.remove(i)
        ans += 1 if len(rest) < 23 else find_subset_of_length_n(rest)
    return ans