from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 2:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 69