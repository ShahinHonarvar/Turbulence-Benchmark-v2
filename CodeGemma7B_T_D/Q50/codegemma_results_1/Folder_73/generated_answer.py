from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list]
    str_dict = defaultdict(list)
    for string in str_list:
        count = 0
        sorted_str = sorted(string)
        for char in sorted_str:
            count += char.isalpha()
        str_dict[count].append(sorted_str)
    num_anagrams = 0
    for key, value in str_dict.items():
        if len(value) >= 2:
            num_anagrams += len(value) * (len(value) - 1) // 2
    return num_anagrams >= 91