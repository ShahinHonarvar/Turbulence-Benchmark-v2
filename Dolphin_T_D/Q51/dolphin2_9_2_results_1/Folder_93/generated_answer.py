import sortedcontainers

def if_contains_anagrams(strings):
    freq_map = {}
    for string in strings:
        if len(string) < 3:
            continue
        key = tuple(sorted(string.lower()))
        freq_map[key] = freq_map.get(key, 0) + 1
    frequency = list(freq_map.values())
    frequency.sort(reverse=True)
    if len(frequency) > 1 and frequency[0] > 2 * frequency[1]:
        return False
    return True