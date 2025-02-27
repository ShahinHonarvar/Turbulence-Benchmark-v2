def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s))

    def is_anagram(s1, s2):
        return sorted_string(s1) == sorted_string(s2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 81:
                    return False
    return anagram_count <= 81