def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_lower(strings[i]) == sorted_lower(strings[j]):
                    anagram_pairs_count += 1
                    if anagram_pairs_count > 5:
                        return False
    return True