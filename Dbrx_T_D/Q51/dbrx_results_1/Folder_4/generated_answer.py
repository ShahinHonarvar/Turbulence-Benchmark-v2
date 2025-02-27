from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams_count = 0
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 3:
            anagrams_count += len(anagram) * (len(anagram) - 1) // 2
            if anagrams_count > 84:
                return False
    return True