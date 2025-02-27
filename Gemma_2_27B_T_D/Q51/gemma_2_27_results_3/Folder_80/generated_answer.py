from collections import Counter

def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                a = Counter(words[i].lower())
                b = Counter(words[j].lower())
                if a == b:
                    count += 1
    return count <= 255