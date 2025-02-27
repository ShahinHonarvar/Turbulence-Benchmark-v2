from collections import Counter

def if_contains_anagrams(strings):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    sorted_strings = [sort_chars(s) for s in strings if len(s) >= 3]
    counts = Counter(sorted_strings)
    for count in counts.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 29