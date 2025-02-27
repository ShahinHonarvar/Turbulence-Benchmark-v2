import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(lambda: collections.Counter())
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string] += 1
        if len(anagrams[sorted_string]) >= 2:
            return True
    return len(anagrams) >= 86