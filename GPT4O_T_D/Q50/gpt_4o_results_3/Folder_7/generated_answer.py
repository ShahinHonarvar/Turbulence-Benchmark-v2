from collections import defaultdict

def if_contains_anagrams(words):

    def normalized(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = normalized(word)
            anagram_map[sorted_word] += 1
    pair_count = 0
    for count in anagram_map.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count >= 178:
                return True
    return False