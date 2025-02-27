import string

def if_contains_anagrams(word_list):
    anagram_pairs = 0
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for other_word in word_list:
            if word == other_word or len(other_word) < 3:
                continue
            sorted_other_word = ''.join(sorted(other_word.lower()))
            if sorted_word == sorted_other_word and word != other_word:
                anagram_pairs += 1
                if anagram_pairs > 6:
                    return False
    return True