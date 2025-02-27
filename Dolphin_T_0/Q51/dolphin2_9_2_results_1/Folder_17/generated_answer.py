from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = ''.join(sorted(lst[i].lower()))
            word2 = ''.join(sorted(lst[j].lower()))
            if len(word1) >= 3 and len(word2) >= 3 and (word1 == word2):
                count += 1
    return count <= 22