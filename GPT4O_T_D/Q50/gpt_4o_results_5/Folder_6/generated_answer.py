from collections import defaultdict

def if_contains_anagrams(strings):
    char_signature_map = defaultdict(list)
    for word in strings:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            char_signature_map[sorted_word].append(word_lower)
    anagram_pairs = 0
    for words in char_signature_map.values():
        if len(words) >= 2:
            anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs >= 26