def if_contains_anagrams(strings):

    def count_anagrams(strings):
        anagram_count = 0
        sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
        seen = set()
        for s in sorted_strings:
            if s in seen:
                anagram_count += 1
            seen.add(s)
        return anagram_count
    return count_anagrams(strings) >= 29