def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) < 3:
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
            if len(anagram_dict[sorted_word]) == 2:
                count += 1
        else:
            anagram_dict[sorted_word] = [word]
    return count >= 8