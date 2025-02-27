def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 75:
            return True
    return False