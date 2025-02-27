def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))

    def is_valid_pair(s1, s2):
        return s1 != s2 and len(s1) >= 3 and (len(s2) >= 3)
    count = 0
    canonical_forms = [canonical_form(s) for s in strings]
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_pair(strings[i], strings[j]) and canonical_forms[i] == canonical_forms[j]:
                count += 1
                if count > 40:
                    return False
    return count <= 40