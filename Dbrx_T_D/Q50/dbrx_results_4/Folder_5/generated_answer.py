import re

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = re.sub('\\\\W+', '', word).lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = {word}
        else:
            anagrams[sorted_word].add(word)
    anagram_pairs = sum((len(ana) * (len(ana) - 1) // 2 for ana in anagrams.values()))
    return anagram_pairs >= 21