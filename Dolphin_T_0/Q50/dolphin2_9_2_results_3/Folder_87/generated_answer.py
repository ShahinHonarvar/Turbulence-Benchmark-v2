def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def get_anagram_pairs(lst):
        return sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if is_anagram(lst[i], lst[j])))
    return get_anagram_pairs([''.join(sorted(s.lower())) for s in lst if len(s) >= 3]) >= 88