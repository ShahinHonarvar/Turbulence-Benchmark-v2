def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    anagram_count = 0
    anagram_pairs = set()
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            sorted_i = sorted_chars(strings[i])
            sorted_j = sorted_chars(strings[j])
            if len(sorted_i) >= 3 and sorted_i == sorted_j:
                anagram_pairs.add(tuple(sorted([strings[i].lower(), strings[j].lower()])))
                if len(anagram_pairs) > 26:
                    return False
    return len(anagram_pairs) <= 26