def find_subset_of_length_n(s):
    return len(select_subsets(s, 380))

def select_subsets(s, n):
    if n == 0:
        return [[]]
    result = []
    for x in s:
        for y in select_subsets(s, n - 1):
            result.append([x] + y)
    return result