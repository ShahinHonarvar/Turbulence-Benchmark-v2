def if_contains_anagrams(lst):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    n = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                n += 1
    return n >= 47