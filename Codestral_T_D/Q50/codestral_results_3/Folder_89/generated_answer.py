def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                count += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1
    return count >= 36