def find_subset_of_length_n(s):
    ans = 0
    n = len(s)
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if i & 1 << j != 0]
        if len(subset) == 21:
            ans += 1
    return ans