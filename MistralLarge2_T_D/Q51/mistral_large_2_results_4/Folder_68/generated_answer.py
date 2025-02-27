from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    counted_anagrams = defaultdict(int)
    anagram_pairs = 0
    for i, s1 in enumerate(strings):
        if len(s1) < 3:
            continue
        for s2 in strings[i + 1:]:
            if len(s2) < 3 and is_anagram(s1, s2):
                counted_anagrams[tuple(sorted(s1.lower()))] += 1
                if counted_anagrams[tuple(sorted(s1.lower()))] == 2:
                    anagram_pairs += 1
                    if anagram_pairs > 94:
                        return False
    return anagram_pairs <= 94