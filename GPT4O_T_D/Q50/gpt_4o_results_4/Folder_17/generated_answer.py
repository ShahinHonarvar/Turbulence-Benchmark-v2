def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return sorted_str(s1) == sorted_str(s2) and len(s1) >= 3
    anagrams = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagrams.append((lst[i], lst[j]))
                if len(anagrams) >= 97:
                    return True
    return False