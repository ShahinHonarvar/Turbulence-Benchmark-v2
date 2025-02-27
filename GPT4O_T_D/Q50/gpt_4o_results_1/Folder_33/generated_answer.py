from collections import defaultdict

def if_contains_anagrams(words):

    def sort_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_word(word)
            anagram_count[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 140