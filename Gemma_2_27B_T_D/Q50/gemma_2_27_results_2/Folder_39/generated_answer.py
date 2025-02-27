from collections import Counter

def if_contains_anagrams(strings):
    anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1) == Counter(s2)):
                anagrams += 1
    return anagrams >= 54