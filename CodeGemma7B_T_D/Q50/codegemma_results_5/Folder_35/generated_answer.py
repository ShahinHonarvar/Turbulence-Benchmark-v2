from collections import defaultdict

def if_contains_anagrams(text_list):
    text_list = [word.lower() for word in text_list]
    for word in text_list:
        if len(word) < 3:
            text_list.remove(word)
    dict_str = defaultdict(list)
    for string in text_list:
        dict_str[''.join(sorted(string))].append(string)
    result = [key for key, value in dict_str.items() if len(value) >= 153]
    return len(result) > 0