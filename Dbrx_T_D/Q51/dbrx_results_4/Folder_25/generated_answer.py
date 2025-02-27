import string

def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        elif sorted_word in anagrams:
            anagrams[sorted_word].append(word)
            count += len(anagrams[sorted_word]) - 1
            if count > 67:
                return False
    return True