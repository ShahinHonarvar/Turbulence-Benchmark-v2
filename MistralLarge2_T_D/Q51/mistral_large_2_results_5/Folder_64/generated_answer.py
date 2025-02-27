from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count > 59:
                return False
    return True