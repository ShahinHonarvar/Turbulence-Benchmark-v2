import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = sorted(word.lower())
        sorted_word = ''.join(sorted_word)
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs >= 58