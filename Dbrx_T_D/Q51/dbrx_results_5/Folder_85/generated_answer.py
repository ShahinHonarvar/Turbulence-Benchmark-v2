from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for string in strings:
        if len(string) < 3 or not set(string) <= english_letters:
            continue
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    return sum((len(pair) > 1 for pair in anagrams.values())) <= 276