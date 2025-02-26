from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    anagram_count = 0
    for word in string_list:
        filtered_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(filtered_word) >= 3:
            sorted_word = ''.join(sorted(filtered_word))
            anagram_groups[sorted_word].append(word)
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 98