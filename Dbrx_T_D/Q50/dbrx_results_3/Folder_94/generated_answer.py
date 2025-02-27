import itertools

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string_length in range(3, len(max(list_of_strings, key=len)) + 1):
        strings_of_length = [s for s in list_of_strings if len(s) == string_length]
        sorted_strings = [''.join(sorted(s)) for s in strings_of_length]
        for _, group in itertools.groupby(sorted(sorted_strings)):
            anagrams_count += len(list(group)) - 1
            if anagrams_count >= 46:
                return True
    return False