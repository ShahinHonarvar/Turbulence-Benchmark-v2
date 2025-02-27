import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] == 1:
                    return True
            else:
                anagrams[sorted_word] = 0
    return False