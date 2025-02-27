def if_contains_anagrams(strings):

    def sorted_tuple(s):
        return tuple(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3]
    seen = {}
    count = 0
    for string in filtered_strings:
        key = sorted_tuple(string)
        if key in seen:
            count += seen[key]
            seen[key] += 1
        else:
            seen[key] = 1
    return count <= 55