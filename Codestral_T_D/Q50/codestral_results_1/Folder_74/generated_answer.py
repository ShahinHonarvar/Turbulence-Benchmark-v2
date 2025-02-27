def if_contains_anagrams(words):
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if count >= 17:
                return True
    return False