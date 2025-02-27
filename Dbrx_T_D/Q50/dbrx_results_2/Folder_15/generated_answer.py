import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for value in anagrams.values():
        if len(value) >= 4:
            count += 1
    return count >= 1