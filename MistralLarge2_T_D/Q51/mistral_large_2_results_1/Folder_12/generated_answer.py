from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and (j, i) not in checked_pairs:
                if are_anagrams(strings[i], strings[j]) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    checked_pairs.add((j, i))
    return anagram_count <= 92