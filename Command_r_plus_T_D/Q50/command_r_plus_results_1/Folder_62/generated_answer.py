def if_contains_anagrams(lst):
    anagram_count = 0
    word_set = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word not in word_set:
            word_set.add(sorted_word)
            for other_word in lst:
                if word != other_word and sorted_word == ''.join(sorted(other_word.lower())):
                    anagram_count += 1
                    break
    return anagram_count >= 43