def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted_string(s1) == sorted_string(s2))
    count = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 84:
                    return False
    return True