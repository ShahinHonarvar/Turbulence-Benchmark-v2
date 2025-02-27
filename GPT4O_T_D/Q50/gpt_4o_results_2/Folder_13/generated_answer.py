from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_anagrams = defaultdict(int)
    for word in strings:
        wl = len(word)
        if wl < 3:
            continue
        key = ''.join(sorted(word.lower()))
        valid_anagrams[key] += 1
    count_pairs = 0
    for value in valid_anagrams.values():
        if value > 1:
            count_pairs += value * (value - 1) // 2
    return count_pairs >= 144