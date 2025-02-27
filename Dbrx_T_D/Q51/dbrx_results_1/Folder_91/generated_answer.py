from collections import Counter

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string in string_list:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if Counter(sorted_string) in anagram_counts:
            anagram_counts[Counter(sorted_string)] += 1
            if anagram_counts[Counter(sorted_string)] > 2:
                anagrams_count += 1
                if anagrams_count > 88:
                    return False
        else:
            anagram_counts[Counter(sorted_string)] = 1
    return True