from itertools import combinations

def all_substring_of_size_n(text):
    res = list(combinations(text, 73))
    result_list = list(set([''.join(i) for i in res]))
    return result_list if result_list else []