def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1_filtered = ''.join((c.lower() for c in s1 if c.isalpha()))
        s2_filtered = ''.join((c.lower() for c in s2 if c.isalpha()))
        return len(s1_filtered) >= 3 and len(s2_filtered) >= 3 and (sorted(s1_filtered) == sorted(s2_filtered))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 34:
                    return False
    return True