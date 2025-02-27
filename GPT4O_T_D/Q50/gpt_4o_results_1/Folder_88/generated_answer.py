def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_lower(s)
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s] += 1
            else:
                anagram_groups[sorted_s] = 1
    count = 0
    for val in anagram_groups.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 34:
                return True
    return False