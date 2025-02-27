import string

def if_contains_anagrams(words):
    anagrams = set()
    for word in [x.lower() for x in words]:
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams.add(sorted_word)
    return len(anagrams) <= 41