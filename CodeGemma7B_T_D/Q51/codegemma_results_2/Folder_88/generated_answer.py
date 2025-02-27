def if_contains_anagrams(str_list):
    anagrams = {}

    def is_anagram(s):
        return ''.join(sorted(s.lower()))
    for s in str_list:
        key = is_anagram(s)
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return sum((v for v in anagrams.values())) <= 407