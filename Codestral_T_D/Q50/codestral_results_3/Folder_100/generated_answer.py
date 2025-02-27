def if_contains_anagrams(strs):
    anagram_count = 0
    anagram_dict = {}
    for word in strs:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_count += len(anagram_dict[sorted_word])
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    return anagram_count >= 95