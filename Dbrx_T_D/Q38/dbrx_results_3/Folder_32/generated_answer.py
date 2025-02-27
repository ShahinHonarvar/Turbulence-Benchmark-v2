def find_subset_of_length_n(s, n):
    if n < 0 or (n == 0 and s):
        return 0
    elif n == 0 and (not s):
        return 1
    else:
        element = list(s)[0]
        s.remove(element)
        return find_subset_of_length_n(s, n - 1) + find_subset_of_length_n(s, n)