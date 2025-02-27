from collections import Counter

def if_contains_anagrams(lst):
    values = []
    for string in lst:
        if len(string) >= 3:
            c = Counter(string.lower())
            values.append(c)
    counter = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                counter += 1
    return counter / 2 <= 66