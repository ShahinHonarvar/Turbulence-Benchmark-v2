def if_contains_anagrams(strings):

    def sort_and_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for string in strings:
        if len(string) >= 3:
            key = sort_and_lower(''.join(filter(str.isalpha, string)))
            if key in anagram_groups:
                anagram_groups[key].append(string)
            else:
                anagram_groups[key] = [string]
    anagram_pairs_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs_count <= 61