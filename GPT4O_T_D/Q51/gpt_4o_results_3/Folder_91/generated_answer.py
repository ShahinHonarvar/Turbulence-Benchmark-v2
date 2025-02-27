from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
    anagram_pairs = 0
    for count in word_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 88:
            return False
    return True