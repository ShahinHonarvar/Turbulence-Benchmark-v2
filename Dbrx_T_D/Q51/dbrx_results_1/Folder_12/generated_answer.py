import string

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and all((char in string.ascii_letters for char in sorted_string)):
            anagrams.append(sorted_string)
    anagram_pairs = len(anagrams) - len(set(anagrams))
    return anagram_pairs <= 92