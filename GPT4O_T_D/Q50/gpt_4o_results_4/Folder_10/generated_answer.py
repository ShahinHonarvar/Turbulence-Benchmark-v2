def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            canonical_form = ''.join(sorted(s.lower()))
            if canonical_form in anagram_dict:
                count += anagram_dict[canonical_form]
                anagram_dict[canonical_form] += 1
            else:
                anagram_dict[canonical_form] = 1
            if count >= 52:
                return True
    return False