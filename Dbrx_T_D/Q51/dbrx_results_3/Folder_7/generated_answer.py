import string

def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                if anagrams[sorted_word] < 445:
                    anagrams[sorted_word] += 1
                    count += 1
            else:
                anagrams[sorted_word] = 1
    return count <= 445