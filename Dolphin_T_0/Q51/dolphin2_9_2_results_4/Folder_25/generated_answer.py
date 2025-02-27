from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                count += 1
    return count <= 67