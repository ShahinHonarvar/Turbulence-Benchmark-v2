def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    length_filtered = [s for s in strings if len(s) >= 3]
    for i in range(len(length_filtered)):
        for j in range(i + 1, len(length_filtered)):
            if sorted_lower(length_filtered[i]) == sorted_lower(length_filtered[j]):
                anagram_count += 1
                if anagram_count > 38:
                    return False
    return True