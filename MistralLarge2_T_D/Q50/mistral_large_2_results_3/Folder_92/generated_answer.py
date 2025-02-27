from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += 1
            if count >= 2:
                return True
    return False