from collections import defaultdict, Counter

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    str_dict_counter = defaultdict(defaultdict)
    for i in range(len(str_list)):
        str_dict[len(str_list[i])].append(str_list[i].lower())
    for key, value in str_dict.items():
        for string in value:
            str_dict_counter[key][Counter(string)].append(string)
    for key, value in str_dict_counter.items():
        if key >= 3:
            if len(value) >= 47:
                if len(value) % 2 == 0:
                    return True
                elif value.get(Counter(value[0])) is not None and len(value) - 1 != len(value.get(Counter(value[0]))) + 1:
                    return True
    return False