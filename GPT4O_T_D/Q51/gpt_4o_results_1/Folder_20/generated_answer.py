from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    normalized = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    counts = Counter(normalized)
    for count in counts.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 131:
                return False
    return True