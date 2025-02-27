def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    count = 0
    for word in anagram_dict:
        count += anagram_dict[word] * (anagram_dict[word] - 1) // 2
        if count >= 11:
            return True
    return False