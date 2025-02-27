import collections

def if_contains_anagrams(str_list):
    str_dict = collections.defaultdict(list)
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        str_dict[word].append(word)
    num_anagrams = sum((len(value) for value in str_dict.values() if len(value) > 2))
    return num_anagrams <= 74