def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = word
    return len(anagrams) <= 392