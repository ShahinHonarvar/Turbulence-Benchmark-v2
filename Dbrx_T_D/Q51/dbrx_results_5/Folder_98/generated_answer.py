import string

def if_contains_anagrams(words):
    anagrams = set()
    alphabet = set(string.ascii_lowercase)
    for word in words:
        word = word.lower()
        if len(word) < 3 or not set(word).issubset(alphabet):
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams.discard(sorted_word)
            if len(anagrams) > 46:
                return True
        else:
            anagrams.add(sorted_word)
    return False