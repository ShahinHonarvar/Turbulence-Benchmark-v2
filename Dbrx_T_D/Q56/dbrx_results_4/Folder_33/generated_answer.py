from itertools import permutations

def all_substring_of_size_n(input_string):
    result = set()
    for n in range(1, len(input_string)):
        for perm in permutations(input_string, n):
            substring = ''.join(perm)
            if len(substring) == 105 and len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)