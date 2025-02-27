from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    caches = {}
    for word in strings:
        word = str(word).lower()
        if len(word) >= 3 and word in caches:
            continue
        if len(word) >= 3:
            for i in range(len(strings)):
                if i != strings.index(word) and Counter(word) == Counter(strings[i].lower()):
                    count += 1
                    caches[word] = None
    return True if count <= 85 else False