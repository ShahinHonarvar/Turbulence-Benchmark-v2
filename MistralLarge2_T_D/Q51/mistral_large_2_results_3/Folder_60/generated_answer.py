from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            count_pairs += len(value) * (len(value) - 1) // 2
    return count_pairs <= 77