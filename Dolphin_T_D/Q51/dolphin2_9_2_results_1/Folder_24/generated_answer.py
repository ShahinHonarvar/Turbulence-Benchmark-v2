from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = Counter()
    for string in list_of_strings:
        if len(string) >= 3:
            count[tuple(sorted(string.lower()))] += 1
    return count.most_common(1)[0][1] <= 96