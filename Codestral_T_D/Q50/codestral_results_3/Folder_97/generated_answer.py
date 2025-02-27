def if_contains_anagrams(lst):
    anagram_count = 0
    dict_anagram = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in dict_anagram:
                dict_anagram[sorted_word] = [word]
            else:
                dict_anagram[sorted_word].append(word)
                anagram_count += 1
    return anagram_count >= 123