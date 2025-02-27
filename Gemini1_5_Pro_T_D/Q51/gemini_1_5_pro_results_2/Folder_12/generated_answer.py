import itertools

def if_contains_anagrams(list_of_strings):
    count = 0
    for string_pair in itertools.combinations(list_of_strings, 2):
        if len(string_pair[0]) >= 3 and len(string_pair[1]) >= 3 and (sorted(string_pair[0].lower()) == sorted(string_pair[1].lower())):
            count += 1
    if count <= 92:
        return True
    else:
        return False