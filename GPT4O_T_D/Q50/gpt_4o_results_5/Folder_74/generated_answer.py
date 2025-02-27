from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counter = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            anagram_counter[sorted_word] += 1
    total_pairs = 0
    for count in anagram_counter.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs >= 17:
            return True
    return False