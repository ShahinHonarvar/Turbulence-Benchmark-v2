from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_counts = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_counts:
            anagram_counts[sorted_word] += 1
        else:
            anagram_counts[sorted_word] = 1
    for count in anagram_counts.values():
        if count > 26:
            return False
    return True