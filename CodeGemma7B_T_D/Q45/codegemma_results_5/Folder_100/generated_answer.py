def palindromes_between_indices(given_string):
    modified_str = given_string.lower().replace(' ', '')
    unique_letters = set(modified_str[0:6])
    return {''.join(p) for p in itertools.permutations(unique_letters, len(unique_letters)) if p[0] == p[-1] or p[0] + p[1] == p[-1] - p[-2]}