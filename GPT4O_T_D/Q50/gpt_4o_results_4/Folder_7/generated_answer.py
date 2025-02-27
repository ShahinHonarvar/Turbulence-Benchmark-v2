from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sort_word(s)
            anagram_count[key] += 1
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 178