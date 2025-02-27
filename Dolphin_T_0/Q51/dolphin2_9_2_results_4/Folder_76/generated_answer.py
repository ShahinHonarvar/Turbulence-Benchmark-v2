from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            str1 = Counter(strings[i].lower())
            str2 = Counter(strings[j].lower())
            if str1 == str2:
                pairs += 1
                if pairs >= 91:
                    return True
    return False