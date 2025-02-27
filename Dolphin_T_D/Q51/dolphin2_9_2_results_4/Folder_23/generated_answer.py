from collections import Counter

def if_contains_anagrams(strings):
    count = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in count:
                count[sorted_string] += 1
            else:
                count[sorted_string] = 1
    num_anagrams = sum((value >= 2 for value in count.values()))
    return num_anagrams <= 49