import string

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string1 in list_of_strings:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower().translate(str.maketrans('', '', string.punctuation))))
        for string2 in list_of_strings:
            if string1 == string2:
                continue
            sorted_string2 = ''.join(sorted(string2.lower().translate(str.maketrans('', '', string.punctuation))))
            if sorted_string1 == sorted_string2:
                anagrams_count += 1
                break
    return anagrams_count >= 188