from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_count = 0
    checked = defaultdict(set)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[j] not in checked[strings[i]] and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                checked[strings[i]].add(strings[j])
                if anagram_count > 97:
                    return False
    return True