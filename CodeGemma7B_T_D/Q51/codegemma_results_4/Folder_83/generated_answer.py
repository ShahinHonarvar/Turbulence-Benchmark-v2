def if_contains_anagrams(str_list):
    anagrams = set()
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) < 3:
            continue
        if string in anagrams:
            return False
        anagrams.add(string)
    return len(anagrams) <= 19