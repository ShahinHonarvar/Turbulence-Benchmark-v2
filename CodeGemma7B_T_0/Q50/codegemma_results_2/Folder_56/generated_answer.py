def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return sum((count >= 77 for count in anagrams.values())) >= 1