def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = 0
    for values in anagram_dict.values():
        if len(values) > 1:
            anagram_pairs += len(values) * (len(values) - 1) // 2
            if anagram_pairs > 64:
                return False
    return True