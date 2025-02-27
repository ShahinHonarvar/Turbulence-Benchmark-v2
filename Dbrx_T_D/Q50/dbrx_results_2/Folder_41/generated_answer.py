import string

def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        elif len(word) >= 3:
            anagrams[sorted_word] = [word]
    pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return pairs >= 75