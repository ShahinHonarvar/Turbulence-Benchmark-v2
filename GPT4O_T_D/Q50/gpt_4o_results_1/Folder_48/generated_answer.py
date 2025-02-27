from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            key = sorted_chars(word)
            anagram_dict[key] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 219