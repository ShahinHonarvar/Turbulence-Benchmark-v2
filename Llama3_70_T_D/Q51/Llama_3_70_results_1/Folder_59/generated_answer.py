from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        cleaned_string = ''.join(filter(str.isalpha, string)).lower()
        if len(cleaned_string) >= 3:
            sorted_string = ''.join(sorted(cleaned_string))
            anagrams[sorted_string] += 1
    pairs = sum(anagrams.values()) - len(anagrams)
    return pairs <= 15