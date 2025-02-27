def if_contains_anagrams(strings):

    def sort_chars(s):
        return ''.join(sorted(s))
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_chars = sort_chars(s)
            if sorted_chars not in anagrams:
                anagrams[sorted_chars] = 0
            anagrams[sorted_chars] += 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 8