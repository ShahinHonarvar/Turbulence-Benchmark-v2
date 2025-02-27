def if_contains_anagrams(lst):
    counter = 0
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                counter += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1
    return counter >= 66