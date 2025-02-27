def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))

    def is_anagram(s1, s2):
        return sort_string(s1) == sort_string(s2) and len(s1) >= 3
    count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    n = len(sorted_strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(sorted_strings[i], sorted_strings[j]):
                count += 1
                if count > 48:
                    return False
    return True