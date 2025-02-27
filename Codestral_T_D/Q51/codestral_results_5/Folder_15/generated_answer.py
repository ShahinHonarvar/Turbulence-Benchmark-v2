from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(lower_string)
        else:
            anagrams[sorted_string] = [lower_string]
    count = 0
    for values in anagrams.values():
        if len(values) >= 2:
            count += len(values) * (len(values) - 1) // 2
            if count > 20:
                return False
    return True