def if_contains_anagrams(list_of_str):
    anagrams = set()
    for word in list_of_str:
        word = word.lower()
        sort_word = ''.join(sorted(word))
        if sort_word not in anagrams:
            anagrams.add(sort_word)
        elif len(anagrams) == 18:
            return False
    return True