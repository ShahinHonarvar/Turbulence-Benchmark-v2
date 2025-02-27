def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_count += 1
            if anagram_count >= 115:
                return True
        else:
            anagram_dict[sorted_word] = word
    return False