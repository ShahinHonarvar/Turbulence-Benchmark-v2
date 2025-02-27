def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    num_pairs = 0
    for anagram_list in anagrams.values():
        num_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    if num_pairs >= 75:
        return True
    else:
        return False