def find_subset_of_length_n(a):
    n = len(a)
    result = 0
    for i in range(2 ** n):
        subset = set()
        for j in range(n):
            if i >> j & 1:
                subset.add(a[j])
        if len(subset) == 78:
            result += 1
    return result