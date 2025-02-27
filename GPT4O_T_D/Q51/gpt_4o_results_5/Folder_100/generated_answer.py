from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted((c for c in word.lower() if c.isalpha())))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_count[normalized_word] += 1
    pair_count = 0
    for count in anagram_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count > 98:
                return False
    return pair_count <= 98