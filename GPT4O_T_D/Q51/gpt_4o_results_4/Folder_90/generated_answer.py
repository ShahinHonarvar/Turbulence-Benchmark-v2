from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_count = 0
    normalized_dict = defaultdict(list)
    for s in str_list:
        normalized_str = ''.join(sorted((c.lower() for c in s if c.isalpha())))
        if len(normalized_str) >= 3:
            normalized_dict[normalized_str].append(s)
    for key, value_list in normalized_dict.items():
        n = len(value_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count > 147:
            return False
    return True