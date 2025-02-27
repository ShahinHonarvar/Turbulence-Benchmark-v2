def find_subset_of_length_n(my_set):
    n = len(my_set)
    count = 0
    for i in range(n + 1):
        count += binomial_coefficient(n, i)
    return count

def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k == 1 or k == n - 1:
        return n
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)