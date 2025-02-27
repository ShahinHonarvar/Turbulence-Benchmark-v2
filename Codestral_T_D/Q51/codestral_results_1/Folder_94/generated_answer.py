def if_contains_anagrams(strings):

    def count_anagrams(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for string in strings:
        if len(string) < 3:
            continue
        anagram = count_anagrams(string)
        if anagram in anagram_count:
            anagram_count[anagram] += 1
        else:
            anagram_count[anagram] = 1
    count = 0
    for anagram in anagram_count:
        count += anagram_count[anagram] * (anagram_count[anagram] - 1) // 2
    return count <= 181