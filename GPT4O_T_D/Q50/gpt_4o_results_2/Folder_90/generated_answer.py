from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    count = 0
    for group_count in anagram_groups.values():
        if group_count > 1:
            count += group_count * (group_count - 1) // 2
        if count >= 177:
            return True
    return False