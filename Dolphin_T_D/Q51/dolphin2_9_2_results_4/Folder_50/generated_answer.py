from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    string_set = set([''.join(sorted(s.lower())) for s in strings if len(s) >= 3])
    string_dict = {s: string_set.count(s) for s in string_set}
    for key in string_dict:
        if string_dict[key] > 1:
            count += string_dict[key] - 1
            if count > 47:
                return False
    return True