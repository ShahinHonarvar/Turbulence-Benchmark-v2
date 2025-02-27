import itertools

def palindromes_between_indices(string):
    result_set = set()
    for indices in itertools.product(range(2, 6), repeat=4):
        temp_set = set()
        for sub_indices in itertools.product(*indices):
            sub_str = ''.join([string[i] for i in sub_indices])
            temp_set.add(sub_str)
        if sorted(temp_set) == sorted(temp_set, reverse=True):
            result_set.update(temp_set)
    return result_set