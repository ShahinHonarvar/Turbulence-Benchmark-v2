from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for group in anagram_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count >= 81