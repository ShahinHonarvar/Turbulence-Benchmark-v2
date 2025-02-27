def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        lower = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(lower))
        if len(lower) < 3 or not lower.isalpha():
            continue
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs = 0
    for count in anagrams_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs <= 24