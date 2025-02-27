from functools import reduce

def palindromes_between_indices(input_string):
    chars = sorted(set(input_string[0:8].lower()))
    return set(reduce(lambda acc, l: acc + [p + l + p[::-1] for p in acc], chars, ['']))