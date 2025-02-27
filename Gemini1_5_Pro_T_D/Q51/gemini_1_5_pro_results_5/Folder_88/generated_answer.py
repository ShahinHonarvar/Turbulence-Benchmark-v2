from collections import Counter
  import itertools

def if_contains_anagrams(list_of_strings):

    def is_anagram(first_string, second_string):
        return Counter(first_string.lower()) == Counter(second_string.lower())
    count = 0
    for first_string, second_string in itertools.combinations(list_of_strings, 2):
        if len(first_string) >= 3 and len(second_string) >= 3 and is_anagram(first_string, second_string):
            count += 1
    return count <= 407