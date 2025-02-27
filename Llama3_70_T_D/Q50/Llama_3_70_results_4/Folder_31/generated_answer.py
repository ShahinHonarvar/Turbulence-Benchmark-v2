def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                count += len(anagram_dict[sorted_word])
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    return count >= 68