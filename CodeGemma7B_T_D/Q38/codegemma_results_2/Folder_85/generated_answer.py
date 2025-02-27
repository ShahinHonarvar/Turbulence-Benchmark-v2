from itertools import combinations

def find_subset_of_length_n(set):
    output = 0
    arr = list(set)
    for i in range(n):
        output += len(list(combinations(arr, i)))
    return output