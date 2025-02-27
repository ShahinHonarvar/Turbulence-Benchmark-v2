def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s))
    anagram_map = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            key = sorted_str(string.lower())
            if key in anagram_map:
                count += anagram_map[key]
                anagram_map[key] += 1
            else:
                anagram_map[key] = 1
    return count >= 72