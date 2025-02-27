import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for value in anagrams.values():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
            if count >= 7:
                return True
    return False