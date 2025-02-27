import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3 or any((char.isdigit() for char in sorted_word)):
            continue
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return sum((len(value) > 1 for value in anagrams.values())) <= 24