from collections import Counter

def if_contains_anagrams(strings_list):
    if len(strings_list) < 411 * 2:
        return False
    anagrams_counter = Counter((''.join(sorted(word.lower())) for word in strings_list if len(word) >= 3))
    for anagrams_num in anagrams_counter.values():
        if anagrams_num > 1:
            return True
    return False