import itertools
  from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for first_string_index, second_string_index in itertools.combinations(range(len(list_of_strings)), 2):
        if len(list_of_strings[first_string_index]) >= 3 and len(list_of_strings[second_string_index]) >= 3:
            if Counter(list_of_strings[first_string_index].lower()) == Counter(list_of_strings[second_string_index].lower()):
                anagram_count += 1
    if anagram_count <= 366:
        return True
    else:
        return False