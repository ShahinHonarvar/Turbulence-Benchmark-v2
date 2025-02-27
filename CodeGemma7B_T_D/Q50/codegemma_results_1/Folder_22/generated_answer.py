from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list if len(s) >= 3]
    seen_anagrams = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string))
        if sorted_string in seen_anagrams:
            seen_anagrams[sorted_string].append(string)
        else:
            seen_anagrams[sorted_string] = [string]
    return len(seen_anagrams) >= 72