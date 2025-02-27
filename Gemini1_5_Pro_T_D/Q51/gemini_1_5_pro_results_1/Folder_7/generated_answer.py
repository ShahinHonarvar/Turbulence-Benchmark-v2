import itertools

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string_pair in itertools.combinations(list_of_strings, 2):
        if len(string_pair[0]) >= 3 and len(string_pair[1]) >= 3 and (len(string_pair[0]) == len(string_pair[1])):
            if sorted(string_pair[0].lower()) == sorted(string_pair[1].lower()):
                anagram_count += 1
    if anagram_count <= 445:
        return True
    else:
        return False