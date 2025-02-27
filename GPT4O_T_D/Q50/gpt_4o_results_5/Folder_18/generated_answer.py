def if_contains_anagrams(strings):
    anagram_count = 0
    words_dict = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in words_dict:
                anagram_count += words_dict[sorted_word]
                words_dict[sorted_word] += 1
            else:
                words_dict[sorted_word] = 1
            if anagram_count >= 106:
                return True
    return False