from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_characters(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_key = sorted_characters(word)
            anagram_dict[anagram_key] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 22:
            return True
    return False