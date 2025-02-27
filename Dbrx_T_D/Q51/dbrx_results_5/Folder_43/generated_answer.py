import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    if len(anagrams.values()) > 3:
        return False
    for freq in anagrams.values():
        if freq > 3:
            return False
    return True