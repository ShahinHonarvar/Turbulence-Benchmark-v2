def find_subset_of_length_n(set_a):
    length = len(set_a)
    s = [1] * len(set_a)
    result = 1
    for i in range(len(set_a)):
        for j in range(i):
            s[j] += s[j] * (i - j)
        if set_a[i] <= n:
            result += s[i]
    return result