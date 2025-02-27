def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if normalize_string(lst[i]) == normalize_string(lst[j]):
                    anagram_pairs.append((lst[i], lst[j]))
    return len(anagram_pairs) <= 6