def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word] += 1
        else:
            word_dict[sorted_word] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_dict.values() if count > 1))
    return anagram_pairs >= 65