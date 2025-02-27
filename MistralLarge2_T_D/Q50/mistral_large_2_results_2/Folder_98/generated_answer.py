from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    pairs_count = 0
    for count in anagram_count.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count >= 7