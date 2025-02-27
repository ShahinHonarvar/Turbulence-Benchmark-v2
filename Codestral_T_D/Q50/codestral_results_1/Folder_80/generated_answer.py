from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 19