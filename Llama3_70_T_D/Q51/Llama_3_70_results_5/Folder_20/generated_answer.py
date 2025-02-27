def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagram_dict:
            count += 1
            if count > 131:
                return False
        else:
            anagram_dict[sorted_word] = True
    return True