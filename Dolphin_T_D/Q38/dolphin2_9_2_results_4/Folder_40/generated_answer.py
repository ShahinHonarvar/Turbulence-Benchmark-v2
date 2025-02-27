def find_subset_of_length_n(s, n):
    if n == 0:
        return 1
    elif n > 0 and (not s):
        return 0
    else:
        return find_subset_of_length_n(s - {s.pop()}, n - 1) + find_subset_of_length_n(s, n)