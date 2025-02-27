from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    checked_pairs = set()
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                pair = tuple(sorted([strings[i].lower(), strings[j].lower()]))
                if pair not in checked_pairs and is_anagram(strings[i], strings[j]):
                    checked_pairs.add(pair)
                    count += 1
                    if count > 77:
                        return False
    return True