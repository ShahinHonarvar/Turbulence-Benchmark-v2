from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    normalized_words = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            normalized_words[sorted_word] += 1
    for count in normalized_words.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 73