from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        groups[sorted_string].append(string)
    count = 0
    for key, value in groups.items():
        n = len(value)
        if n >= 2:
            count += n * (n - 1) // 2
    if count <= 18:
        return True
    else:
        return False