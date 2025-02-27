def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
                anagram_count += len(anagram_dict[sorted_word]) - 1
            else:
                anagram_dict[sorted_word] = [lower_word]
    return anagram_count <= 72