from collections import Counter

def if_contains_anagrams(s):
    count = 0
    for i in range(len(s)):
        if len(s[i]) >= 3:
            for j in range(i + 1, len(s)):
                if len(s[j]) >= 3 and Counter(s[i].lower()) == Counter(s[j].lower()):
                    count += 1
                    if count >= 189:
                        return True
    return False