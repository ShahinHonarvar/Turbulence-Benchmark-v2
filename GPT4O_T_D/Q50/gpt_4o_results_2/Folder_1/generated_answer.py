def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s)
            if key in anagram_counts:
                count += anagram_counts[key]
                anagram_counts[key] += 1
            else:
                anagram_counts[key] = 1
    return count >= 96