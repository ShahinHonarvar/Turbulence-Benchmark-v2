from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counter = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_counter[sorted_string] += 1
        if anagram_counter[sorted_string] > 96:
            return True
    return False