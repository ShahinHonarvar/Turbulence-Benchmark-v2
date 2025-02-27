from collections import defaultdict

def if_contains_anagrams(str_list):
    str_cache = defaultdict(int)
    length_cache = defaultdict(int)
    unique_length = set()
    for string in str_list:
        if len(string) >= 3:
            str_cache[string.lower()] += 1
            length_cache[len(string)] += 1
            unique_length.add(len(string))
    for i in sorted(unique_length):
        for j in range(i, i + i // 2 + 1):
            if j in str_cache and i - j in str_cache:
                if j in length_cache and i - j in length_cache:
                    if str_cache[j] * str_cache[i - j] >= 188:
                        return True
    return False