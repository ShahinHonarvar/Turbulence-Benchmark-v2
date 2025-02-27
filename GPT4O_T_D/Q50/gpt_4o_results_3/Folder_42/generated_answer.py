def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    anagram_pairs = 0
    for count in word_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 233