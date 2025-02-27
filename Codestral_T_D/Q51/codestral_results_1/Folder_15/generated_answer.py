def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = 1
            else:
                anagrams[sorted_s] += 1
    anagram_pairs = sum([n * (n - 1) // 2 for n in anagrams.values()])
    return anagram_pairs <= 20