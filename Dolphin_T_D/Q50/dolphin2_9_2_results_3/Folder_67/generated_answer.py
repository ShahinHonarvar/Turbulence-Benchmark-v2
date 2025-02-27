def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return sorted(s1) == sorted(s2)
    pair_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if is_anagram(lst[i], lst[j]):
                pair_count += 1
                if pair_count >= 41:
                    return True
    return False