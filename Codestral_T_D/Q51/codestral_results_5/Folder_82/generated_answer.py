from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    for key in anagrams_dict:
        if len(anagrams_dict[key]) > 1:
            count += len(anagrams_dict[key]) * (len(anagrams_dict[key]) - 1) // 2
    return count <= 40