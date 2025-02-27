from collections import Counter

def if_contains_anagrams(str_list):
    data_list = []
    for word in str_list:
        temp_str = sorted(word.lower())
        temp_str = ''.join(temp_str)
        data_list.append(temp_str)
    count_list = list(Counter(data_list).values())
    count_list.sort(reverse=True)
    if len(count_list) >= 14 and count_list[0] >= 14:
        return True
    else:
        return False