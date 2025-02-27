import itertools

def if_contains_anagrams(strings_list):
    anagrams_list = []
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_list.append(sorted_string)
    anagrams_count = 0
    for anagram in set(anagrams_list):
        if anagrams_list.count(anagram) > 1:
            anagrams_count += 1
    return anagrams_count >= 58