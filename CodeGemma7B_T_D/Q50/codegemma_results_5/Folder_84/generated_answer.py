def if_contains_anagrams(str_list):
    anagrams = set()
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.add(sorted_word)
    return len(anagrams) >= 108