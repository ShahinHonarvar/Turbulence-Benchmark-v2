from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key in anagram_dict:
        anagram_list = anagram_dict[key]
        if len(anagram_list) > 1:
            anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
        if anagram_pairs > 69:
            return False
    return True