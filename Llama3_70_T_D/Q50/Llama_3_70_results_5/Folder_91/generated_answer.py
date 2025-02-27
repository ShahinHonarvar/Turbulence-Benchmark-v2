def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    sorted_strings = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            if sorted_s in sorted_strings:
                sorted_strings[sorted_s] += 1
            else:
                sorted_strings[sorted_s] = 1
    for count in sorted_strings.values():
        anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 6