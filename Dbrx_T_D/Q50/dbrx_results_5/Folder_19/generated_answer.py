import string

def if_contains_anagrams(list_of_strings):
    anagrams_dictionary = {}
    for word in list_of_strings:
        if len(word) >= 3:
            word = word.lower()
            word = ''.join((c for c in word if c not in string.punctuation))
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_dictionary:
                anagrams_dictionary[sorted_word].append(word)
            else:
                anagrams_dictionary[sorted_word] = [word]
    total_anagrams = 0
    for anagrams_list in anagrams_dictionary.values():
        if len(anagrams_list) >= 2:
            total_anagrams += len(anagrams_list)
    return True if total_anagrams >= 84 else False