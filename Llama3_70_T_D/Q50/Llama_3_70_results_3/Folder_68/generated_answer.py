def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word_lower)
        else:
            anagram_dict[sorted_word] = [word_lower]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            n = len(anagram_dict[key])
            count += n * (n - 1) // 2
    return count >= 9