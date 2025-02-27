from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    anagram_count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    for count in counter.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 475