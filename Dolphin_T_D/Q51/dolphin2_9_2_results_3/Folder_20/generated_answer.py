def if_contains_anagrams(lst):
    strings = [s.lower() for s in lst if len(s) >= 3]

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    pair_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                pair_count += 1
    return pair_count <= 131