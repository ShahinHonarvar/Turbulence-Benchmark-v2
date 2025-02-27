from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word] += 1
    count = 0
    for word_count in anagram_count.values():
        count += word_count * (word_count - 1) // 2
    return count <= 210