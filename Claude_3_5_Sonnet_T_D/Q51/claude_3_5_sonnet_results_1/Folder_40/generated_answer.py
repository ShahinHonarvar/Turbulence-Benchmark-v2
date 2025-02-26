from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_strings = {}
    for s in string_list:
        cleaned_s = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned_s) >= 3:
            sorted_s = ''.join(sorted(cleaned_s))
            if sorted_s in processed_strings:
                anagram_count += 1
                if anagram_count > 29:
                    return False
            else:
                processed_strings[sorted_s] = True
    return True