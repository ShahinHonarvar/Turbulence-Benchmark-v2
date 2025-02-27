def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_chars(strings[i]) == sorted_chars(strings[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 22:
                        return False
    return True