def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    sorted_strings = [(i, sorted_chars(word)) for i, word in enumerate(strings) if len(word) >= 3]
    sorted_strings.sort(key=lambda x: x[1])
    for i in range(len(sorted_strings)):
        j = i + 1
        while j < len(sorted_strings) and sorted_strings[i][1] == sorted_strings[j][1]:
            anagram_pairs += 1
            if anagram_pairs > 86:
                return False
            j += 1
    return True