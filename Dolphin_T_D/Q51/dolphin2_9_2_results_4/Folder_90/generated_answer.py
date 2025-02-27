import itertools

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for i in range(len(word)):
                for j in range(i + 1, len(word)):
                    if sorted(word[i].lower()) == sorted(word[j].lower()):
                        count += 1
    return count <= 147