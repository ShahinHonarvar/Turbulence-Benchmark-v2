from collections import defaultdict

def if_contains_anagrams(words):

    def sort_chars(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_chars(word)
            anagram_map[sorted_word] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += sum(range(count))
            if anagram_pairs > 54:
                return False
    return True