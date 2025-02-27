from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    count = 0
    for list_of_anagrams in anagrams.values():
        if len(list_of_anagrams) >= 3:
            count += len(list_of_anagrams) * (len(list_of_anagrams) - 1) // 2
    return count >= 77