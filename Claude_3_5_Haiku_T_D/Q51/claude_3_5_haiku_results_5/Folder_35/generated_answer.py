def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = ''.join((c for c in s1.lower() if c.isalpha()))
        s2 = ''.join((c for c in s2.lower() if c.isalpha()))
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2))
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 210:
                    return False
    return True