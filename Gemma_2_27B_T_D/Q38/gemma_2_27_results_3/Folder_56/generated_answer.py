def find_subset_of_length_n(s):
    n = len(s)
    count = 0
    for i in range(1 << n):
        subset = set()
        for j in range(n):
            if i >> j & 1:
                subset.add(set(s)[j])
        if len(subset) == 60:
            count += 1
    return count