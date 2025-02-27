def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                anagram_dict[sorted_word] += 1
                anagram_count += anagram_dict[sorted_word] - 1
    return anagram_count >= 18