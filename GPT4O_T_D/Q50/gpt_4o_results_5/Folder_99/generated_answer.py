from collections import Counter

def if_contains_anagrams(strings):

    def sort_str(s):
        return ''.join(sorted(s))
    formatted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    counted_anagrams = Counter(formatted_strings)
    for count in counted_anagrams.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 314