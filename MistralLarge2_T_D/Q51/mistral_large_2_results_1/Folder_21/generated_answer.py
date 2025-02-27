from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1, s2 = (strings[i], strings[j])
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_pairs.add((min(s1.lower(), s2.lower()), max(s1.lower(), s2.lower())))
    return len(anagram_pairs) <= 26