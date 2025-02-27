import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return count <= 318