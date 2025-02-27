def if_contains_anagrams(str_list):
    anagrams = set()
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if string in anagrams:
            return False
        anagrams.add(string)
    return len(anagrams) <= 43