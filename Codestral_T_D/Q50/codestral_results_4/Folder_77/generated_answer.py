def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 209