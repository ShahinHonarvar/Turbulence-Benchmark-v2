def if_contains_anagrams(words):
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(lower_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 16