def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_lower(string)
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    count_pairs = 0
    for count in anagrams.values():
        if count > 1:
            count_pairs += count * (count - 1) // 2
        if count_pairs >= 29:
            return True
    return False