def if_contains_anagrams(lst):

    def sort_and_convert(s):
        return ''.join(sorted(s.lower()))
    count_anagrams = {}
    for s in lst:
        if len(s) >= 3:
            sorted_s = sort_and_convert(s)
            if sorted_s in count_anagrams:
                count_anagrams[sorted_s] += 1
            else:
                count_anagrams[sorted_s] = 1
    num_pairs = sum((v * (v - 1) // 2 for v in count_anagrams.values() if v > 1))
    return num_pairs <= 116