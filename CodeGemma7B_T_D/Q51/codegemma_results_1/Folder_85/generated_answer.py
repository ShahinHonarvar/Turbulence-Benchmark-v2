def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    return len(anagrams) <= 276