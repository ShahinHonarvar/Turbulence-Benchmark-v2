def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
            else:
                anagram_groups[sorted_string] = [string]
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) >= 3:
            anagram_count += 1
            if anagram_count >= 3:
                return True
    return False