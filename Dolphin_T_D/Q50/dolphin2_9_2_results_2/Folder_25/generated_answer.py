def if_contains_anagrams(lst):
    anagram_pairs_count = 0
    anagram_dict = {}
    for word in lst:
        clean_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and clean_word not in anagram_dict:
            anagram_dict[clean_word] = [word]
        elif len(word) >= 3 and clean_word in anagram_dict and (word not in anagram_dict[clean_word]):
            anagram_dict[clean_word].append(word)
            anagram_pairs_count += 1
            if anagram_pairs_count == 14:
                return True
    if anagram_pairs_count >= 14:
        return True
    return False