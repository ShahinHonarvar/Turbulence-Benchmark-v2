def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        word = ''.join(sorted(word))
        if word in anagrams:
            anagrams[word] += 1
        else:
            anagrams[word] = 1
    for anagram in anagrams.values():
        if anagram >= 2:
            return True
    return False