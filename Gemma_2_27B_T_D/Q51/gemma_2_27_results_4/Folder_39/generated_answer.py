from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(Counter(strings[i].lower()).items()) == sorted(Counter(strings[j].lower()).items()):
                    count += 1
    return count <= 257