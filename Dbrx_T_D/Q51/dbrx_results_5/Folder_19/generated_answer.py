import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        if len(word.lower()) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams.append(sorted_word)
    return len(anagrams) <= 69