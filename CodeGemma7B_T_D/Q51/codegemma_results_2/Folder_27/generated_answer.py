def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        anagram_key = ''.join(sorted(word.lower()))
        if anagram_key not in anagram_dict:
            anagram_dict[anagram_key] = set()
        anagram_dict[anagram_key].add(word)
    return len(anagram_dict) <= 113