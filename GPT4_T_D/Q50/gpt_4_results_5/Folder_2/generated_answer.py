from collections import defaultdict

def if_contains_anagrams(strings):
    strings_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            strings_dict[''.join(sorted(string.lower()))].append(string)
    anagrams_count = sum((len(values) * (len(values) - 1) // 2 for values in strings_dict.values() if len(values) > 1))
    return anagrams_count >= 246