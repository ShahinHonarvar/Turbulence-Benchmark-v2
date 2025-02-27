import itertools

def if_contains_anagrams(strings_list):
    anagrams_list = []
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_list.append(sorted_string)
    anagrams_count = sum((1 for _ in itertools.combinations(anagrams_list, 2) if _[0] == _[1]))
    return anagrams_count >= 178