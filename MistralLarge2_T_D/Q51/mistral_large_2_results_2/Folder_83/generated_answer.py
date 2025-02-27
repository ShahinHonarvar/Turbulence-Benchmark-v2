from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if is_anagram(strings[i], strings[j]):
                if (i, j) not in checked and (j, i) not in checked:
                    anagram_count += 1
                    checked.add((i, j))
                    checked.add((j, i))
            if anagram_count > 19:
                return False
    return anagram_count <= 19