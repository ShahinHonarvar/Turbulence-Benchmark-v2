from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 72