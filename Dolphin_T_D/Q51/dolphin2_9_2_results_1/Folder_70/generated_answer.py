from collections import Counter

def if_contains_anagrams(lst):
    pair_count = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c = Counter(word)
            for i in range(len(lst)):
                if lst[i] != word:
                    lst[i] = lst[i].lower()
                    d = Counter(lst[i])
                    if c == d:
                        pair_count += 1
                        break
    return pair_count <= 97