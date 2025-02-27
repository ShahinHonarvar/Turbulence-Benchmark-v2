def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key not in anagram_dict:
            anagram_dict[key] = [word]
        else:
            anagram_dict[key].append(word)
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 97 and all((len(word) >= 3 for word in anagram_list)):
            return True
    return False