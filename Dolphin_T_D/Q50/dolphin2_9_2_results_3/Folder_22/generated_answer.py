from collections import Counter

def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = ''.join(sorted(strings[i].lower()))
            s2 = ''.join(sorted(strings[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1) == Counter(s2)):
                anagrams_count += 1
                if anagrams_count >= 72:
                    return True
    return False