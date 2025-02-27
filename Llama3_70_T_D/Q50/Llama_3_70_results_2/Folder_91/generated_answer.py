def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(lower_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    count = 0
    for value in anagram_dict.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 6