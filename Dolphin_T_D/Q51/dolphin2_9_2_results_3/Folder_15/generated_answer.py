from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            counter = Counter(word.lower())
            key = ''.join(sorted(counter))
            if key in anagrams:
                anagrams[key] += 1
                count += 1
            else:
                anagrams[key] = 1
    return count <= 20