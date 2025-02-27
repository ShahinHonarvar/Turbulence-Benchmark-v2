from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_dict[key].append(word)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs <= 89