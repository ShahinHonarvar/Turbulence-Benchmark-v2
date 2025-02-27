from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    processed = [tuple(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = Counter(processed)
    for count in counter.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 93:
            return True
    return False