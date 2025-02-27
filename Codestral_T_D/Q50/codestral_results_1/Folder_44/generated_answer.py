def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
                anagram_count += len(anagram_dict[sorted_word]) - 1
            else:
                anagram_dict[sorted_word] = [word]
    return anagram_count >= 44