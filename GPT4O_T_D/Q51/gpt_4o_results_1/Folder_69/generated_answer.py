def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return canonical_form(s1) == canonical_form(s2) and len(s1) >= 3
    pairs_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                pairs_count += 1
                if pairs_count > 58:
                    return False
    return True