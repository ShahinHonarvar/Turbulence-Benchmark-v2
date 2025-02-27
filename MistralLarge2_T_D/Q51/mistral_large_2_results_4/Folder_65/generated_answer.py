from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    checked = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked and (j, i) not in checked and (len(strings[i]) >= 3) and (len(strings[j]) >= 3):
                if is_anagram(strings[i], strings[j]):
                    count += 1
                    checked.add((i, j))
                    checked.add((j, i))
                    if count > 72:
                        return False
    return True