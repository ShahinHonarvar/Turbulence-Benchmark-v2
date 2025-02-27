from collections import defaultdict

def if_contains_anagrams(lst):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                pair = tuple(sorted([lst[i].lower(), lst[j].lower()]))
                if pair not in checked_pairs:
                    if are_anagrams(lst[i], lst[j]):
                        anagram_count += 1
                        checked_pairs.add(pair)
                    if anagram_count > 61:
                        return False
    return True