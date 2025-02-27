from itertools import combinations

def all_substring_of_size_n(str):
    str = str.replace('0', '').replace('.', '')
    substring_list = [''.join(comb) for comb in combinations(str, 17)]
    result = list({s for s in substring_list if len(set(s)) == len(s)})
    return result if result else []