def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) < 3:
            continue
        if sorted_word in anagram_dict:
            count += 1
        else:
            anagram_dict[sorted_word] = word
    return count >= 77