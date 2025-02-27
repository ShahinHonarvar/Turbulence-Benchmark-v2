import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            elif anagrams[sorted_word] < 257:
                anagrams[sorted_word] += 1
            else:
                return False
    return True