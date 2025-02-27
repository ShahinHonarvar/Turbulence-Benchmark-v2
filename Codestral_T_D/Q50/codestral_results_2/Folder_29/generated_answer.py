from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 35