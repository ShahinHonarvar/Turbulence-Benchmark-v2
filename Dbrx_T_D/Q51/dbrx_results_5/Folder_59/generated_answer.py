import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower().translate(str.maketrans('', '', string.punctuation)))).split()
        if len(sorted_string) >= 3:
            sorted_string = ''.join(sorted_string)
            if sorted_string in anagrams:
                return True
            anagrams.add(sorted_string)
    return len(anagrams) > 15