def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 314:
            return True
    return False