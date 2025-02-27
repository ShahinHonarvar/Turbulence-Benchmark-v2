import string

def if_contains_anagrams(string_list):
    english_letters = set(string.ascii_letters.lower())
    anagrams_dict = {}
    for word in string_list:
        word = word.lower()
        if len(word) < 3 or not set(word).issubset(english_letters):
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word] += 1
            if anagrams_dict[sorted_word] > 9:
                return False
        else:
            anagrams_dict[sorted_word] = 1
    return True