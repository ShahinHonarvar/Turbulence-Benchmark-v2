from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) / 2
    if count <= 116:
        return True
    else:
        return False