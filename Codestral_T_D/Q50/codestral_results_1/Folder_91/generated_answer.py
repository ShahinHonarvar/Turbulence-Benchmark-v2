def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2 and len(key) >= 3:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if anagram_count >= 6:
                return True
    return False