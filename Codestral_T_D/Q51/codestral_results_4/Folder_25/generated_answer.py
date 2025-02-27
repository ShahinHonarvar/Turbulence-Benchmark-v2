from collections import defaultdict

def if_contains_anagrams(strings):
    grouped_anagrams = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            grouped_anagrams[key].append(s)
    anagram_pairs = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in grouped_anagrams.values()))
    return anagram_pairs <= 67