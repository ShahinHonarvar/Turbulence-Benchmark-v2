from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    count_pairs = 0
    for word in strings:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_count[sorted_word] += 1
    for count in anagram_count.values():
        count_pairs += count * (count - 1) // 2
        if count_pairs >= 77:
            return True
    return False