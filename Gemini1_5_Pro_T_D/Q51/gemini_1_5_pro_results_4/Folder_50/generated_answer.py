from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(lambda: [])
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
        if count > 47:
            return True
    return False