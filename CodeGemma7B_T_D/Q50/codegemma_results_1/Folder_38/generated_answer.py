def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        elif len(sorted_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word].append(word)
    for key, value in anagrams.items():
        if len(value) >= 24:
            return True
    return False