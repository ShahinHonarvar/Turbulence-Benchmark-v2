from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_counts = Counter(anagrams)
    for count in anagram_counts.values():
        if count >= 2:
            pairs_needed = 6 - (len(anagram_counts) - list(anagram_counts.values()).count(1))
            if pairs_needed <= 0:
                return True
    return False