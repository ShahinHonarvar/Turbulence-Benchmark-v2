def if_contains_anagrams(lst):

    def anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())

    def length_three_plus(s):
        return len(s) >= 3
    return len([(i, j) for i in lst for j in lst if anagram(i, j) and length_three_plus(i) and length_three_plus(j)]) >= 66