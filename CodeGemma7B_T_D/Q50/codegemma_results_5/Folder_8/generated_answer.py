def if_contains_anagrams(str_list):
    anagrams = []
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        for anagram in anagrams:
            if sorted_word == anagram:
                break
        else:
            anagrams.append(sorted_word)
    return len(anagrams) >= 85