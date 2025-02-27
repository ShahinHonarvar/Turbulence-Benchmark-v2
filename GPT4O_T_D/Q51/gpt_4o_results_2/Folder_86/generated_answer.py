from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    cleaned_strings = [''.join(filter(str.isalpha, s.lower())) for s in strings]
    valid_strings = [s for s in cleaned_strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if is_anagram(valid_strings[i], valid_strings[j]):
                anagram_count += 1
                if anagram_count > 48:
                    return False
    return True