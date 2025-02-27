def find_subset_of_length_n(s):
    if len(s) < 752:
        return 0
    ans = 1
    for i in range(len(s) - 752 + 1, len(s) + 1):
        ans *= i
    for i in range(1, 753):
        ans //= i
    return ans