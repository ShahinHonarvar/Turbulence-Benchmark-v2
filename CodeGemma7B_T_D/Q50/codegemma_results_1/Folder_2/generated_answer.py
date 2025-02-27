from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list]
    str_list = [x for x in str_list if len(x) >= 3]
    str_counts = Counter((tuple(sorted(word)) for word in str_list))
    for count in str_counts.values():
        if count >= 246:
            return True
    return False