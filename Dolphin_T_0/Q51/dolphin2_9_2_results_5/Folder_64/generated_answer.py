from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    pair_count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            counter[sorted_string] += 1
            pair_count += counter[sorted_string] - 1
            if pair_count > 59:
                return False
    return True