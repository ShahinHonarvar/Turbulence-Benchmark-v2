from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(filter(str.isalpha, word.lower())))
    anagram_count = 0
    seen = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        sorted_w = sorted_word(word)
        seen[sorted_w] += 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 24