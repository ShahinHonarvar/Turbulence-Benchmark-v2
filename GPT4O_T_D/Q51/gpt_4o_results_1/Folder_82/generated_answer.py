from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = normalize(''.join(filter(str.isalpha, s)))
            anagram_dict[key].append(s)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n > 1:
            count += n * (n - 1) // 2
    return count <= 40