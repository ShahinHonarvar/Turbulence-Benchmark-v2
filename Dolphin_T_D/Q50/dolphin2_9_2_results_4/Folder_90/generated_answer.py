import collections

def if_contains_anagrams(list_of_strings):
    list_of_strings_lower = [s.lower() for s in list_of_strings if len(s) >= 3]
    grouped_by_length = {}
    for s in list_of_strings_lower:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in grouped_by_length:
            grouped_by_length[sorted_s] = []
        grouped_by_length[sorted_s].append(s)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in grouped_by_length.values() if len(v) > 1))
    return anagram_count >= 177