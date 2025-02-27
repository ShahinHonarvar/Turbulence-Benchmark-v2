def if_contains_anagrams(words):
    anagram_dict = {}
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                count += anagram_dict[sorted_word]
                if count >= 49:
                    return True
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    return False