def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_string(strings[i]) == sorted_string(strings[j]):
                    anagram_pairs += 1
                    if anagram_pairs >= 59:
                        return True
    return False