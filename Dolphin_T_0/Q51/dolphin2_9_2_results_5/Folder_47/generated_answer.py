from collections import Counter

def if_contains_anagrams(lst):
    count_anagrams = 0
    counter = Counter()
    for string in lst:
        if len(string) >= 3:
            string_lower = string.lower()
            sorted_string = ''.join(sorted(string_lower))
            counter[sorted_string] += 1
    for letter_count in counter.values():
        count_anagrams += letter_count * (letter_count - 1)
    return count_anagrams <= 366