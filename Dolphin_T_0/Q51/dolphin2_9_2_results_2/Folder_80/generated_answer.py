def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for other_word in list_of_strings:
                if word != other_word and len(other_word) >= 3:
                    sorted_other_word = ''.join(sorted(other_word.lower()))
                    if sorted_word == sorted_other_word:
                        anagram_pairs += 1
    if anagram_pairs > 255:
        return False
    else:
        return True