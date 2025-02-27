import string

def if_contains_anagrams(word_list):
    anagrams = {}
    alpha = string.ascii_letters
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower())).translate(str.maketrans('', '', alpha))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] > 25:
                    return False
            else:
                anagrams[sorted_word] = 1
    return True