import itertools

def if_contains_anagrams(list_of_strings):
    counter = 0
    for first_string_index, second_string_index in itertools.combinations(range(len(list_of_strings)), 2):
        if len(list_of_strings[first_string_index]) >= 3 and len(list_of_strings[second_string_index]) >= 3 and (sorted(list_of_strings[first_string_index].lower()) == sorted(list_of_strings[second_string_index].lower())):
            counter += 1
    return counter <= 147