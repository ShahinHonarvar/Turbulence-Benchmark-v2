def find_subset_of_length_n(s):
    if str(type(s)) != "<class 'set'>":
        return 0
    elements = list(s)
    num_of_subsets = 1 << len(elements)
    cnt = 0
    for i in range(num_of_subsets):
        subset = [elements[j] for j in range(len(elements)) if i & 1 << j]
        if len(subset) == 72:
            cnt += 1
    return cnt