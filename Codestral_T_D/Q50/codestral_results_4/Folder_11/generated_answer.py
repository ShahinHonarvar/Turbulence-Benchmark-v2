def if_contains_anagrams(strings):
    anagram_count = {}
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_count:
                anagram_count[sorted_string] += 1
            else:
                anagram_count[sorted_string] = 1
            if anagram_count[sorted_string] >= 2:
                count += 1
    return count >= 28