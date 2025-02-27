from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            c1 = Counter(strings[i].lower())
            c2 = Counter(strings[j].lower())
            if c1 == c2 and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                anagrams.append((strings[i], strings[j]))
    return len(anagrams) <= 48