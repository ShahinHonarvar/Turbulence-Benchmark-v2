from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid(s):
        return len(s) >= 3 and s.isalpha()
    anagram_counts = defaultdict(int)
    valid_strings = [s for s in strings if is_valid(s)]
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if is_anagram(valid_strings[i], valid_strings[j]):
                anagram_counts[i, j] += 1
                if sum(anagram_counts.values()) > 97:
                    return False
    return True