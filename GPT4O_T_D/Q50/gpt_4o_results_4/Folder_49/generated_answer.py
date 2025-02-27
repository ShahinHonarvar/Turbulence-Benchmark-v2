from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    anagram_pairs_count = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs_count += count * (count - 1) // 2
        if anagram_pairs_count >= 59:
            return True
    return False