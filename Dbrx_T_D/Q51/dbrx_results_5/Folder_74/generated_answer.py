import string

def if_contains_anagrams(list_of_strings):
    english_letters = set(string.ascii_lowercase)
    anagrams_count = 0
    for word in list_of_strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in english_letters:
            continue
        for other_word in list_of_strings:
            if word == other_word:
                continue
            sorted_other_word = ''.join(sorted(other_word.lower()))
            if sorted_word == sorted_other_word:
                anagrams_count += 1
                if anagrams_count > 57:
                    return False
    return anagrams_count <= 57