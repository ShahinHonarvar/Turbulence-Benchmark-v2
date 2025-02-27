from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_count[sorted_word] += 1
    return sum((count - 1 for count in anagram_count.values() if count > 1)) >= 194