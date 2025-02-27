from collections import Counter

def if_contains_anagrams(strings):
    counter_dict = Counter()
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter_dict[sorted_word] += 1
    anagram_pairs = 0
    for word, freq in counter_dict.items():
        anagram_pairs += freq * (freq - 1) // 2
    return anagram_pairs >= 36