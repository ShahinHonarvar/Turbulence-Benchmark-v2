def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 59:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = ''.join((c.lower() for c in s1 if c.isalpha()))
    s2 = ''.join((c.lower() for c in s2 if c.isalpha()))
    if len(s1) < 3 or len(s2) < 3 or len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)