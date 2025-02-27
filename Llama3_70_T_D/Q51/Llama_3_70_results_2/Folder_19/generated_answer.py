def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = ''.join(filter(str.isalpha, s1)).lower()
        s2 = ''.join(filter(str.isalpha, s2)).lower()
        return s1 != s2 and sorted(s1) == sorted(s2)
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 69:
                    return False
    return True