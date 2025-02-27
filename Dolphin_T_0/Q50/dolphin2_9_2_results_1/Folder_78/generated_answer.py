from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in a_dict:
                anagram_count += a_dict[sorted_word]
                a_dict[sorted_word] += 1
            else:
                a_dict[sorted_word] = 1
    return anagram_count // 2 >= 79