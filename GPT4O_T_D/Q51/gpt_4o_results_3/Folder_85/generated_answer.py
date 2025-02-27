from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    anagram_pairs = 0
    for anagram_list in word_dict.values():
        n = len(anagram_list)
        anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 276:
            return False
    return True