def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum([len(words) * (len(words) - 1) // 2 for words in anagram_dict.values()])
    return anagram_pairs >= 79