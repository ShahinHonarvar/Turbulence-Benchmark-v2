from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    checked = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (i, j) not in checked and (j, i) not in checked:
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                    count += 1
                    checked.add((i, j))
                    checked.add((j, i))
    return count <= 59