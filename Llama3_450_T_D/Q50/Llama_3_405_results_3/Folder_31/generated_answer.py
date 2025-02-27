def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 68