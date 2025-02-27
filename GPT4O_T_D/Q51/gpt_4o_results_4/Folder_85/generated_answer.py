def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return sorted_string(s1) == sorted_string(s2)
    anagram_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    if anagram_count > 276:
                        return False
    return True