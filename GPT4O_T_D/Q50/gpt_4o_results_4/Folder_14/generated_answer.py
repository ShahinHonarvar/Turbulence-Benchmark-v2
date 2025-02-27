from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs:
                if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                    if is_anagram(strings[i], strings[j]):
                        anagram_count += 1
                        if anagram_count >= 22:
                            return True
                checked_pairs.add((i, j))
    return False