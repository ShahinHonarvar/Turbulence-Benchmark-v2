def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    for val in anagram_dict.values():
        if val > 1:
            count += val * (val - 1) // 2
        if count >= 2:
            return True
    return False