import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string_length in range(3, len(max(strings_list, key=len)) + 1):
        strings_set = {frozenset(s.lower()) for s in strings_list if len(s) == string_length}
        anagrams_count += sum((1 for _ in itertools.combinations(strings_set, 2) if len(_[0] | _[1]) < 2 * string_length))
        if anagrams_count >= 47:
            return True
    return False