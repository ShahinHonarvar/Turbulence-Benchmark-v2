def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    filtered_strings = [s.lower() for s in strings if len(s) >= 3]
    pairs_count = 0
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if is_anagram(filtered_strings[i], filtered_strings[j]):
                pairs_count += 1
                if pairs_count > 66:
                    return False
    return True