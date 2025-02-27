def find_subset_of_length_n(s):
    n = 85
    count = 0
    for i in range(1 << len(s)):
        subset = {element for j, element in enumerate(s) if i & 1 << j}
        if len(subset) == n:
            count += 1
    return count