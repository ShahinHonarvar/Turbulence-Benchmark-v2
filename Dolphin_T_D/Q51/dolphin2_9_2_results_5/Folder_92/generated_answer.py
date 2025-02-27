from collections import Counter

def if_contains_anagrams(lst):
    word_count = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_count:
                word_count[sorted_word] += 1
            else:
                word_count[sorted_word] = 1
            if sorted_word not in word_count:
                word_count[sorted_word] = 0
    anagram_pairs = 0
    for count in word_count.values():
        anagram_pairs += count // 2
        if count % 2 == 1:
            anagram_pairs += 1
    return anagram_pairs <= 68