from itertools import combinations_with_replacement

def all_substring_of_size_n(string):

    def find_all_possible_combinations(possible_letters):
        return [''.join(p) for p in combinations_with_replacement(possible_letters, n)]
    result = set()
    possible_letters = list(set(string))
    for n in range(16, len(possible_letters) + 1):
        for combination in find_all_possible_combinations(possible_letters):
            if len(combination) == n and combination not in result:
                result.add(combination)
    return list(result)