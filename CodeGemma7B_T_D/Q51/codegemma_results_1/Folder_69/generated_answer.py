def if_contains_anagrams(str_list):
    sorted_strings = [sorted(s.lower()) for s in str_list]
    hashmap = {}
    for sorted_str in sorted_strings:
        key = ''.join(sorted_str)
        if key in hashmap:
            if hashmap[key] >= 58:
                return False
            hashmap[key] += 1
        else:
            hashmap[key] = 1
    return True