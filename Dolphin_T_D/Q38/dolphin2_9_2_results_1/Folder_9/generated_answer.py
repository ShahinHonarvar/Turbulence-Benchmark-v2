def find_subset_of_length_n(set_elements):
    count = 0
    for i in range(len(set_elements)):
        combinations = binomial_coeff(len(set_elements), 24)
        count += combinations
    return count

def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res