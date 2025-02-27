def if_contains_anagrams(strings):
    counter = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            counter[sorted_string] = counter.get(sorted_string, 0) + 1
    return sum((count * (count - 1) // 2 for count in counter.values())) <= 4