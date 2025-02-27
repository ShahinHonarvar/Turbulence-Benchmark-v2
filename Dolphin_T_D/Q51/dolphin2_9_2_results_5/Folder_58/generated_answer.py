def if_contains_anagrams(strings_list):

    def lowercase_anagram(s):
        return ''.join(sorted(s.lower()))
    count_anagrams = {}
    for string in strings_list:
        if len(string) >= 3:
            anagram = lowercase_anagram(string)
            if anagram in count_anagrams:
                count_anagrams[anagram] += 1
            else:
                count_anagrams[anagram] = 1
    max_pairs = 0
    for value in count_anagrams.values():
        max_pairs += value // 2
    return max_pairs <= 60