import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string_length in range(3, len(max(string_list, key=len)) + 1):
        string_set = set((''.join(sorted(s)) for s in itertools.combinations(string_list, string_length)))
        anagrams_count += sum((1 for s in string_set if string_list.count(s) > 1))
        if anagrams_count >= 47:
            return True
    return False