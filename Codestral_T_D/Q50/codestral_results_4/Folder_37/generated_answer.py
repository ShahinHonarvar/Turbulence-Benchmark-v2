def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 29