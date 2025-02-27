from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
    count = 0
    for group in anagram_groups.values():
        group_size = len(group)
        if group_size >= 2:
            count += group_size * (group_size - 1) // 2
    return count >= 81