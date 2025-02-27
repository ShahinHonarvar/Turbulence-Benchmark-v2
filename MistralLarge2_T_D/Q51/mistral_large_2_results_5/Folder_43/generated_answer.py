from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_count = defaultdict(int)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word] += 1
    pairs_count = sum((1 for count in anagram_count.values() if count > 1))
    return pairs_count <= 3