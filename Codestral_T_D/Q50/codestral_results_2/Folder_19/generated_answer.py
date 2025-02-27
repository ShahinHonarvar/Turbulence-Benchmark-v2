def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_count += 1
            if anagram_count >= 84:
                return True
        else:
            anagram_dict[sorted_word] = 1
    return False