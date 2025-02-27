import itertools

def if_contains_anagrams(strings_list):
    anagrams = []
    sorted_strings_list = sorted([string.lower() for string in strings_list if len(string) >= 3])
    for string in sorted_strings_list:
        sorted_string = ''.join(sorted(string))
        anagrams.append(sorted_string)
    unique_anagrams_counter = 0
    for anagram in set(anagrams):
        anagram_counter = anagrams.count(anagram)
        if anagram_counter >= 2:
            unique_anagrams_counter += 1
            anagrams.remove(anagram)
    if unique_anagrams_counter >= 277:
        return True
    return False