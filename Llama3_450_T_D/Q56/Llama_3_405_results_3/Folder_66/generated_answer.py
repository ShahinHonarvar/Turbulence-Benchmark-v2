from collections import OrderedDict

def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 25):
        substr = input_string[i:i + 26]
        if len(set(substr)) == 26:
            result.append(substr)
    return list(OrderedDict.fromkeys(result))