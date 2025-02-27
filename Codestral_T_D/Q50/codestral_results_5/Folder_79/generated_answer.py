def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_count += len(anagram_dict[sorted_word])
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    return anagram_count >= 40