def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = word
    return len(anagrams) <= 416