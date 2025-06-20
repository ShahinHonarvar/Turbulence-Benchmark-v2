def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = ''.join(sorted((c.lower() for c in s1 if c.isalpha())))
        s2 = ''.join(sorted((c.lower() for c in s2 if c.isalpha())))
        return len(s1) >= 3 and len(s2) >= 3 and (s1 == s2)
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 73:
                    return False
    return True