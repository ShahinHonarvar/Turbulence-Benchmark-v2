from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 2:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count <= 88