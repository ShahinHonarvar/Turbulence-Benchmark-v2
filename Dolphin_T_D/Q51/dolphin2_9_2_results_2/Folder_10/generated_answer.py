def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3 and key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return max(anagrams.values()) <= 21