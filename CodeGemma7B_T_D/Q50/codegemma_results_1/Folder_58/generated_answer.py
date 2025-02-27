from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                substr = ''.join(sorted(string[i:j + 1].lower()))
                str_dict[substr].append(string)
    num_pairs = 0
    for substr, strings in str_dict.items():
        if len(strings) >= 2:
            num_pairs += len(strings) * (len(strings) - 1) // 2
    return num_pairs >= 411