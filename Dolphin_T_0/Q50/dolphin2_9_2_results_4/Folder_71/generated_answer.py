def if_contains_anagrams(word_list):
    lower_word_list = [word.lower() for word in word_list]
    anagram_pairs = set()
    for word in lower_word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            for other_word in lower_word_list:
                if word != other_word and len(other_word) >= 3 and (sorted_word == ''.join(sorted(other_word))):
                    anagram_pairs.add((word, other_word))
    return len(anagram_pairs) >= 57