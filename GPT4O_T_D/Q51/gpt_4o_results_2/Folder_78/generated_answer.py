from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram(word):
        return len(word) >= 3
    normalized_words = [''.join(sorted(word.lower())) for word in strings]
    anagram_count = defaultdict(int)
    for word in normalized_words:
        if is_valid_anagram(word):
            anagram_count[word] += 1
    num_anagram_pairs = 0
    for count in anagram_count.values():
        if count > 1:
            num_anagram_pairs += count * (count - 1) // 2
    return num_anagram_pairs <= 70