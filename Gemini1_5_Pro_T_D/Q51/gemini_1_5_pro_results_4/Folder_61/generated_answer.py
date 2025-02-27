from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for key, value in anagram_dict.items():
        count += len(value) * (len(value) - 1) // 2
    if count > 50:
        return False
    else:
        return True