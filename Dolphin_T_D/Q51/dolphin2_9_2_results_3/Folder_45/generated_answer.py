from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    seen = set()
    for word in list_of_strings:
        if len(word) < 3:
            continue
        c = Counter(word.lower())
        if all((value == 0 for value in c.values())):
            continue
        sorted_str = ''.join(sorted(c.keys()))
        if sorted_str in seen:
            count += 1
        seen.add(sorted_str)
    return count <= 464