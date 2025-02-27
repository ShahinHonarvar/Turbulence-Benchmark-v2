from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) >= 3:
            c = Counter(sorted(string.lower()))
            for s in strings:
                if len(s) >= 3:
                    if sorted(s.lower()) == list(c):
                        count += 1
    if count <= 49:
        return True
    else:
        return False