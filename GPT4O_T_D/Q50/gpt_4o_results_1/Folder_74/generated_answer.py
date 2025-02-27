from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for anagram_list in anagram_dict.values():
        anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
        if anagram_count >= 17:
            return True
    return False