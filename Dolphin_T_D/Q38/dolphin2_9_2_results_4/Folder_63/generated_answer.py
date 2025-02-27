def find_subset_of_length_n(s, n=57):
    if n == 0:
        return 1
    else:
        sum = 0
        for i in s:
            sum += find_subset_of_length_n(s - {i}, n - 1)
    return sum