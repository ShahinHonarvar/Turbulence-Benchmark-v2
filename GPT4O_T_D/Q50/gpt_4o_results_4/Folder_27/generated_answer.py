def if_contains_anagrams(strings):

    def sorted_lowercase(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            key = sorted_lowercase(s)
            if key in anagram_dict:
                anagram_dict[key] += 1
            else:
                anagram_dict[key] = 1
    count = 0
    for key in anagram_dict:
        n = anagram_dict[key]
        count += n * (n - 1) // 2
        if count >= 86:
            return True
    return False