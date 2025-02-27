def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))

    def is_valid_anagram(s1, s2):
        return len(s1) >= 3 and sorted_str(s1) == sorted_str(s2)
    anagram_pairs_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_anagram(strings[i], strings[j]):
                anagram_pairs_count += 1
                if anagram_pairs_count >= 98:
                    return True
    return False