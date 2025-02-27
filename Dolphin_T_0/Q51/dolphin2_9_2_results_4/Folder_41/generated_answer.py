import collections

def if_contains_anagrams(str_list):
    str_len_at_least_three = [candidates for candidates in str_list if len(candidates) >= 3]
    dict_of_frequencies = collections.Counter([candidates.lower() for candidates in str_len_at_least_three])
    pairs_of_anagrams = sum([v * (v - 1) if v > 1 else 0 for v in dict_of_frequencies.values()])
    return pairs_of_anagrams <= 52