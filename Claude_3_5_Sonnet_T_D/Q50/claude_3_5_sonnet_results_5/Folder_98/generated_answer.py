def if_contains_anagrams(string_list):
    anagram_count = 0
    sorted_words = {}
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_words:
                sorted_words[sorted_word].append(word)
            else:
                sorted_words[sorted_word] = [word]
    for words in sorted_words.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
    return anagram_count >= 7