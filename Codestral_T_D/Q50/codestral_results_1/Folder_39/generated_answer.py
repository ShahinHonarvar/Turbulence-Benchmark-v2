def if_contains_anagrams(string_list):
    count = 0
    anagram_dict = {}
    for word in string_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            count += len(anagram_dict[sorted_word])
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return count >= 54