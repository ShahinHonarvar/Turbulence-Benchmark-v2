from collections import defaultdict

def if_contains_anagrams(lst):
    normalized_words = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            normalized_words[sorted_word] += 1
    anagram_pairs = 0
    for count in normalized_words.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 289:
                return False
    return anagram_pairs <= 289