from collections import defaultdict

def if_contains_anagrams(strings):
    string_dict = defaultdict(int)
    anagram_pairs = 0
    for s in strings:
        filtered_s = ''.join(filter(str.isalpha, s)).lower()
        if len(filtered_s) >= 3:
            sorted_s = ''.join(sorted(filtered_s))
            string_dict[sorted_s] += 1
    for count in string_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 85:
                return False
    return True