from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for word in string_list:
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) >= 3:
            sorted_word = ''.join(sorted(cleaned_word))
            anagram_dict[sorted_word].append(word)
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
        if anagram_count > 14:
            return False
    return True