def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
                if anagram_dict[sorted_word] >= 4:
                    return True
            else:
                anagram_dict[sorted_word] = 1
    return False