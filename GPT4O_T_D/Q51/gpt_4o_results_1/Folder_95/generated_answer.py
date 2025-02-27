from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    count = 0
    seen = set()
    for i in range(len(sorted_strings)):
        if sorted_strings[i] in seen:
            continue
        occurrences = sum((val == sorted_strings[i] for val in sorted_strings))
        count += occurrences * (occurrences - 1) // 2
        if count > 6:
            return False
        seen.add(sorted_strings[i])
    return True