def if_contains_anagrams(lst):

    def is_anagram(a, b):
        a = a.lower()
        b = b.lower()
        return sorted(a) == sorted(b)
    lst = [a for a in lst if len(a) >= 3]
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                return True
    return False