from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word_tuple = tuple(sorted(word.lower()))
            anagram_dict[sorted_word_tuple] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 219:
            return True
    return False