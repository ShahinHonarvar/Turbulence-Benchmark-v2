import string

def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and all((c in string.ascii_letters for c in sorted_word)):
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
    for value in anagrams.values():
        if len(value) > 1:
            count += 1
    return count <= 79