import string

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower())).translate(str.maketrans('', '', string.punctuation))
            if list_of_strings.count(sorted_word) > 1:
                anagrams_count += list_of_strings.count(sorted_word) - 1
                list_of_strings = [x for x in list_of_strings if sorted_word != x]
    return anagrams_count >= 18