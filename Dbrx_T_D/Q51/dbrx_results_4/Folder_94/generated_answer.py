import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_in_list in list_of_strings:
        if len(string_in_list) >= 3:
            sorted_string = ''.join(sorted(string_in_list.lower())).encode('utf-8')
            sorted_string = sorted_string.translate(str.maketrans('', '', string.punctuation.encode('utf-8'))).decode('utf-8')
            anagrams.add(sorted_string)
    return len(anagrams) <= 181