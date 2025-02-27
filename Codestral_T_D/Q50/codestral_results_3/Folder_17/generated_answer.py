def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    count = 0
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count >= 97