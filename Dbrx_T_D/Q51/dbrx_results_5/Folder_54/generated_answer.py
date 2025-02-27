import string

def if_contains_anagrams(words):
    anagrams = {}
    max_count = 39
    for word in words:
        if len(word) < 3 or not word.isalpha():
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    count = sum((len(group) > 1 for group in anagrams.values()))
    return count <= max_count