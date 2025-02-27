def if_contains_anagrams(strings_list):
    anagram_count = 0
    anagram_dict = {}
    for word in strings_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 46