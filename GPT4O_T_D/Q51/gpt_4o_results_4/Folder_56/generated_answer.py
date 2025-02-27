def if_contains_anagrams(lst):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (canonical_form(s1) == canonical_form(s2))
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 11:
                    return False
    return True