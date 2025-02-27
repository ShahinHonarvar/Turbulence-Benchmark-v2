def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s if c.isalpha())))
    processed = [sorted_chars(s.lower()) for s in strings if len(s) >= 3]
    anagram_pairs = sum((processed.count(x) * (processed.count(x) - 1) // 2 for x in set(processed)))
    return anagram_pairs <= 75