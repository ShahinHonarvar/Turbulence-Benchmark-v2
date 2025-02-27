from collections import Counter

def if_contains_anagrams(string_list):
    Max_pairs_of_anagrams = 318
    counter = Counter()
    anagram_counter = 0
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if counter[sorted_string] == 0:
            counter[sorted_string] = 1
        else:
            anagram_counter += 1
            counter[sorted_string] += 1
    return anagram_counter <= Max_pairs_of_anagrams