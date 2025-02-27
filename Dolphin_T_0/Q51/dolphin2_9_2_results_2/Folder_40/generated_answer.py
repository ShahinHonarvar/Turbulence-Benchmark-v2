def if_contains_anagrams(lst):

    def is_anagram(a, b):
        a = a.lower()
        b = b.lower()
        if len(a) < 3 or len(b) < 3:
            return False
        return sorted(a) == sorted(b)
    max_pairs = 29
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs > max_pairs:
                    return False
    return pairs <= max_pairs