def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(string)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 64:
            return True
    return False