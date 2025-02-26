from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if i in processed:
            continue
        s1 = ''.join(filter(str.isalpha, s1.lower()))
        if len(s1) < 3:
            continue
        c1 = Counter(s1)
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            if j in processed:
                continue
            s2 = ''.join(filter(str.isalpha, s2.lower()))
            if len(s2) < 3:
                continue
            if len(s1) == len(s2) and c1 == Counter(s2):
                anagram_count += 1
                processed.add(i)
                processed.add(j)
                if anagram_count > 34:
                    return False
                break
    return True