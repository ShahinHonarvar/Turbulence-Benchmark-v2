def find_subset_of_length_n(s, n):
    if n < 0 or (n > len(s) and len(s) > 0):
        return 0
    elif n == 0 or len(s) == 0:
        return 1
    else:
        return find_subset_of_length_n(s - {s.pop()}, n - 1) + find_subset_of_length_n(s, n)