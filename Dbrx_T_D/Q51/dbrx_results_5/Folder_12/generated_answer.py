import string

def if_contains_anagrams(str_list):
    anagrams = {}
    max_anagrams = 92
    for word in str_list:
        word = word.lower().translate(str.maketrans('', '', string.punctuation))
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] > max_anagrams:
                    return True
            else:
                anagrams[sorted_word] = 1
    return False