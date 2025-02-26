def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_anagram_pair(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (s1.lower() != s2.lower()) and is_anagram(s1, s2)
    anagram_count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_anagram_pair(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 116:
                    return False
    return True