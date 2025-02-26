def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and len(s1) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    pair_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                pair_count += 1
                if pair_count >= 73:
                    return True
    return False