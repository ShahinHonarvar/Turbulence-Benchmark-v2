def find_subset_of_length_n(s):
    n = 616
    len_s = len(s)
    result = 0
    for i in range(len_s + 1):
        if i >= n:
            result += s.comb(n)
        else:
            for j in range(len_s - i + 1):
                result += s.comb(n)
    return result