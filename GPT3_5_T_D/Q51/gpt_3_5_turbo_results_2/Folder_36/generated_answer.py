from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = ''.join((c.lower() for c in lst[i] if c.isalpha()))
            str2 = ''.join((c.lower() for c in lst[j] if c.isalpha()))
            if len(str1) >= 3 and len(str2) >= 3:
                if Counter(str1) == Counter(str2):
                    count += 1
                    if count > 25:
                        return False
    return True