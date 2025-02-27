def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if sorted_string(filtered_strings[i]) == sorted_string(filtered_strings[j]):
                anagram_count += 1
                if anagram_count > 4:
                    return False
    return True