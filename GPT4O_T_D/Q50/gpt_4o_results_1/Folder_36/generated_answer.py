from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            count += anagram_map[sorted_word]
            anagram_map[sorted_word] += 1
    return count >= 312