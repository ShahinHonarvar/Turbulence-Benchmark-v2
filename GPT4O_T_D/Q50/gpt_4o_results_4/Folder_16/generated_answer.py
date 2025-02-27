from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_w = sorted_word(word)
            anagram_dict[sorted_w] += 1
    pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            pairs += count * (count - 1) // 2
        if pairs >= 155:
            return True
    return False