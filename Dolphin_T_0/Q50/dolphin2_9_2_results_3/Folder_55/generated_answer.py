def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return s2.lower() in [''.join(i) for i in permutations(s1.lower())]
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs >= 15:
                    return True
    return pairs >= 15