from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return sorted(w1.lower()) == sorted(w2.lower())
    anagram_count = 0
    seen = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        seen[sorted_word].append(word)
    for group in seen.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 40