from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    potential_anagrams = [s for s in strings if len(s) >= 3]
    sorted_words = [''.join(sorted(s)) for s in potential_anagrams]
    counter = Counter(sorted_words)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs >= 75