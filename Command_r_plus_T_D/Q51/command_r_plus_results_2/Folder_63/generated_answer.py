def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (normalize(lst[i]) == normalize(lst[j])):
                anagram_pairs.add(frozenset({lst[i], lst[j]}))
                anagram_count += 1
                if anagram_count > 423:
                    return False
    return True