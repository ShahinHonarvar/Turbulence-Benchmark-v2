def if_contains_anagrams(str_list):
    anagram_pairs = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.casefold()))
        if sorted_string in anagram_pairs:
            anagram_pairs[sorted_string] += 1
        else:
            anagram_pairs[sorted_string] = 1
    pair_count = 0
    for count in anagram_pairs.values():
        pair_count += count * (count - 1) // 2
    if pair_count <= 113:
        return True
    else:
        return False