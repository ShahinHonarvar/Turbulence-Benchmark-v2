from collections import Counter

def if_contains_anagrams(list_of_strings):
    num_pairs = 0
    for string in list_of_strings:
        if len(string) > 3:
            for comparison_string in list_of_strings:
                if string.lower() != comparison_string.lower():
                    if Counter(string.lower()) == Counter(comparison_string.lower()):
                        num_pairs += 1
    if num_pairs >= 64:
        return True
    else:
        return False