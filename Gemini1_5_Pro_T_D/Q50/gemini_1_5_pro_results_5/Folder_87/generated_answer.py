from itertools import combinations

def if_contains_anagrams(list_of_strings):
    counter = 0
    for first_string, second_string in combinations(list_of_strings, 2):
        if len(first_string) >= 3 and len(second_string) >= 3 and (len(first_string) == len(second_string)):
            if sorted(first_string.lower()) == sorted(second_string.lower()):
                counter += 1
    if counter >= 88:
        return True
    return False