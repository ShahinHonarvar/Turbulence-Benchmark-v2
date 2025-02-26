def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = ''.join((char.lower() for char in s1 if char.isalpha()))
        s2 = ''.join((char.lower() for char in s2 if char.isalpha()))
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 38:
                    return False
    return True