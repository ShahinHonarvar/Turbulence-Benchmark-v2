def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word) < 3 or not sorted_word.isalpha():
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_count = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
    return anagram_count <= 279