from collections import Counter
    from math import comb

def if_contains_anagrams(lst):
    pairs_found = 0
    strings = [''.lower() for string in lst if len(string) >= 3]
    for string in strings:
        sorted_string = ''.join(sorted(string))
        counter = Counter(sorted_string)
        for compare_string in strings:
            if compare_string != string and ''.join(sorted(compare_string)) == sorted_string:
                pairs_found += 1
                strings.remove(compare_string)
                break
    return pairs_found >= comb(len(strings), 2)