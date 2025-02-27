import string

def if_contains_anagrams(word_list):
    anagram_count = 0
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
            if anagram_dict[sorted_word] > 255:
                return False
        else:
            anagram_dict[sorted_word] = 1
    return True