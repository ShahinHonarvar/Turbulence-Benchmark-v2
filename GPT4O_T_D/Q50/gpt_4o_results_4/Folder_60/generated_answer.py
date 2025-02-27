from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    normalized = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if is_anagram(normalized[i], normalized[j]):
                anagram_pairs += 1
                if anagram_pairs >= 60:
                    return True
    return False