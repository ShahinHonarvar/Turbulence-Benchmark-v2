import string

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string_ in list_of_strings:
        sorted_string = ''.join(sorted(string_.lower().replace(' ', '')))
        if len(sorted_string) >= 3 and all((char in string.ascii_letters for char in sorted_string)):
            anagrams.append(sorted_string)
    anagram_counts = {}
    for anagram in anagrams:
        if anagram not in anagram_counts:
            anagram_counts[anagram] = 1
        else:
            anagram_counts[anagram] += 1
    if sum(anagram_counts.values()) > 59 * 2:
        return False
    return True