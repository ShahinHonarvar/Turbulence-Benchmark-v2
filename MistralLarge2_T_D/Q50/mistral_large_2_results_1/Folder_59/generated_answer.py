from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    checked_pairs = set()
    strings = [s for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and (j, i) not in checked_pairs:
                if are_anagrams(strings[i], strings[j]):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    checked_pairs.add((j, i))
    return anagram_count >= 10