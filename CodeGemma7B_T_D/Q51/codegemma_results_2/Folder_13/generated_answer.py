def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams and anagrams[sorted_word] + 1 <= 54:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return len(anagrams) <= 54