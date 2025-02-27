def if_contains_anagrams(strings):

    def normalized(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha())))

    def is_anagram(s1, s2):
        return normalized(s1) == normalized(s2)
    anagram_count = 0
    strings = [s for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 26:
                    return False
    return True