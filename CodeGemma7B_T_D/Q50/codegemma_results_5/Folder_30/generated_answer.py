from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    anagrams = 0
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        str_dict[word].append(word)
        if len(str_dict[word]) >= 78:
            anagrams += 1
    return anagrams >= 78