import string

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string1 in string_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower().translate(str.maketrans('', '', string.punctuation))))
        for string2 in string_list:
            if string1 == string2:
                continue
            sorted_string2 = ''.join(sorted(string2.lower().translate(str.maketrans('', '', string.punctuation))))
            if sorted_string1 == sorted_string2:
                anagram_count += 1
    return anagram_count >= 95