import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = tuple(sorted(word.lower().replace(' ', '')))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            return True
        anagrams.append(sorted_word)
    return len(anagrams) > 407