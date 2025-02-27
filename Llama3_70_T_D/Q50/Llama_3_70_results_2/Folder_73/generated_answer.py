from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_dict = defaultdict(list)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        anagrams_dict[sorted_word].append(word_lower)
    count = 0
    for anagrams in anagrams_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 91