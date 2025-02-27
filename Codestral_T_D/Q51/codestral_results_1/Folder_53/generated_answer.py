def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = sort_string(string)
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 8