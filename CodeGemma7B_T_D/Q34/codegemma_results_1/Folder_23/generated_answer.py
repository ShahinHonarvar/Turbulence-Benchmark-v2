from itertools import combinations

def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41):
    """Returns the smallest set that contains all the given sets."""
    all_sets = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41]
    min_size = float('inf')
    min_set = None
    for size in range(min_size + 1, len(all_sets) + 1):
        for combination in combinations(all_sets, size):
            if all((s.issubset(comb) for s in all_sets for comb in combination)):
                if size < min_size:
                    min_size = size
                    min_set = combination
    return min_set