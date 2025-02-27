from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def is_valid_string(s):
        return len(s) >= 3 and s.isalpha()
    normalized_strings = [s.lower() for s in lst if is_valid_string(s)]
    anagram_pairs = defaultdict(list)
    count_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_anagram(normalized_strings[i], normalized_strings[j]):
                count_pairs += 1
                if count_pairs > 24:
                    return False
    return True