import re

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = re.sub('\\W+', '', word).lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] > 93:
                return True
        else:
            anagrams[sorted_word] = 1
    return False