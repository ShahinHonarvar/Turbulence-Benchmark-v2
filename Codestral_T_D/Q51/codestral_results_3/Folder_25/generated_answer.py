def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if anagram_count > 67:
            return False
    return True