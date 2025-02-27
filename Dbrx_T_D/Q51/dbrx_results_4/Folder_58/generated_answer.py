import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] > 60:
                    return False
            else:
                anagrams[sorted_word] = 1
    return True