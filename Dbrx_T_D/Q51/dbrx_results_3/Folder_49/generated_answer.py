import re

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        word = re.sub('\\W+', '', word)
        sorted_word = ''.join(sorted(word))
        if len(word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    total_anagrams = sum((len(ana) for ana in anagrams.values()))
    return total_anagrams <= 10