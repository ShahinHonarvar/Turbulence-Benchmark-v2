def if_contains_anagrams(words):
    anagram_count = 0
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in word_dict:
            word_dict[sorted_word] += 1
        else:
            word_dict[sorted_word] = 1
    for count in word_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 30