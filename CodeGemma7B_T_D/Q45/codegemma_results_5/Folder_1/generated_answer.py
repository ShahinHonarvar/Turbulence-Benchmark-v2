from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(string):
    filtered_string = string[4:8]
    filtered_string_lower = filtered_string.lower()
    if not filtered_string_lower.isalpha():
        return set()
    letters = [x for x in ascii_lowercase if x in filtered_string_lower]
    unique_letters = list(set(letters))
    permutations_list = set()
    for permutation in permutations(unique_letters):
        perms_str = ''.join(permutation)
        filtered_string = filtered_string_lower.replace(unique_letters[0], perms_str[0], 1)
        filtered_string = filtered_string.replace(unique_letters[1], perms_str[1], 1)
        if filtered_string == filtered_string[::-1]:
            permutations_list.add(filtered_string)
    return permutations_list