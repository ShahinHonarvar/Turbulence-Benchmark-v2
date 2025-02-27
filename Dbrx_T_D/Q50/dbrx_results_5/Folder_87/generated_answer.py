import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string_length in range(3, len(max(strings_list, key=len)) + 1):
        strings_group = itertools.groupby(sorted(strings_list, key=lambda x: x.lower() if len(x) == string_length else ''), lambda x: x.lower() if len(x) == string_length else '')
        for _, group in strings_group:
            if len(list(group)) >= 2:
                anagrams_count += len(list(group)) * (len(list(group)) - 1) // 2
                if anagrams_count >= 88:
                    return True
    return False