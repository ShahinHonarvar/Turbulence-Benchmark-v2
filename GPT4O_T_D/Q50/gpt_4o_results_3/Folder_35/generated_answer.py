from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return pairs >= 153