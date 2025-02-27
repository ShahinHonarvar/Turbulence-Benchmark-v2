from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word] += 1
    pair_count = 0
    for count in anagram_dict.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
        if pair_count >= 61:
            return True
    return False