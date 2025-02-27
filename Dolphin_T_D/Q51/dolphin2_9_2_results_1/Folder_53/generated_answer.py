from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            word_lower = word.lower()
            counter = Counter(word_lower)
            key = ''.join(sorted(word_lower))
            if key in anagrams:
                anagrams[key].append(word_lower)
                if len(anagrams[key]) > 2:
                    return False
            else:
                anagrams[key] = [word_lower]
    return True