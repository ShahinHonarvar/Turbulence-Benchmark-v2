from collections import Counter

def if_contains_anagrams(l):
    anagram_pairs = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if len(l[i]) >= 3 and len(l[j]) >= 3 and (Counter(l[i].lower()) == Counter(l[j].lower())):
                anagram_pairs += 1
                if anagram_pairs >= 58:
                    return True
    return False