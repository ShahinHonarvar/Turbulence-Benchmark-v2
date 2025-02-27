def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))
    norm_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    counted_pairs = 0
    checked_pairs = set()
    for i in range(len(norm_strings)):
        for j in range(i + 1, len(norm_strings)):
            if len(norm_strings[i]) >= 3 and len(norm_strings[j]) >= 3:
                sorted_i = sort_string(norm_strings[i])
                sorted_j = sort_string(norm_strings[j])
                if sorted_i == sorted_j:
                    pair = (i, j)
                    if pair not in checked_pairs:
                        counted_pairs += 1
                        checked_pairs.add(pair)
                        if counted_pairs > 42:
                            return False
    return True