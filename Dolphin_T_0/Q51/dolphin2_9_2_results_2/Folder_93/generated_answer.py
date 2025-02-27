from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            letter_count = Counter(word_lower)
            key = ''.join(sorted(letter_count.keys()))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word_lower)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            pairs = len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
            count += pairs
            if count > 36:
                return False
    return count <= 36