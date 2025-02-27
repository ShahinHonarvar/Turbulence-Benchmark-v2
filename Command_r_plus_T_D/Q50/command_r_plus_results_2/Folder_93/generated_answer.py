def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 2 and len(anagram_list[0]) >= 3:
            count += 1
    return count >= 18