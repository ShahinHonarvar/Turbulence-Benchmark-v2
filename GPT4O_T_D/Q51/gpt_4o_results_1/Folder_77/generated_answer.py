def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    anagram_map = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = sorted_chars(s)
        anagram_map.setdefault(sorted_s, []).append(s)
    count = 0
    for key in anagram_map:
        n = len(anagram_map[key])
        if n > 1:
            count += n * (n - 1) // 2
        if count > 17:
            return False
    return True