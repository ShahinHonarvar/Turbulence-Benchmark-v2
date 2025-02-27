def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for words in anagram_dict.values():
        count += len(words) * (len(words) - 1) // 2
    return count >= 55