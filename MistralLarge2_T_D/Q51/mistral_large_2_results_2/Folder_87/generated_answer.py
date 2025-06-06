from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                pair = tuple(sorted([strings[i].lower(), strings[j].lower()]))
                if pair not in checked_pairs:
                    if is_anagram(strings[i], strings[j]):
                        anagram_count += 1
                        checked_pairs.add(pair)
                    if anagram_count > 392:
                        return False
    return True