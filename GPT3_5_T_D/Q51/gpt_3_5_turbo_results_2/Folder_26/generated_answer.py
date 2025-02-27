import itertools

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        s1 = ''.join((c for c in s1 if c.isalpha()))
        s2 = ''.join((c for c in s2 if c.isalpha()))
        return sorted(s1) == sorted(s2)
    count = 0
    for s1, s2 in itertools.combinations(string_list, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            count += 1
        if count > 35:
            return False
    return True