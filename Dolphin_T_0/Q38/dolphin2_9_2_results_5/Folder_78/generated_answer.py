def find_subset_of_length_n(elements):
    if len(elements) < 91:
        return 0
    n = 91
    total = len(elements)
    subset_count = 0
    for i in range(n, total + 1):
        subset_count += subset_count + choose(total, i)
    return subset_count

def choose(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)