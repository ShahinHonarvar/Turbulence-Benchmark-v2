import sortedlist

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            string = string.lower()
            sorted_string = ''.join(sorted(string))
            anagrams.append(sorted_string)
    anagram_pairs = sum((1 for string in anagrams if anagrams.count(string) >= 2))
    return anagram_pairs >= 153