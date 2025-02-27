from itertools import combinations

def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28):
    for combination in combinations(range(1, 29), 28):
        all_subsets = True
        for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28]:
            if not s.issubset(set(combination)):
                all_subsets = False
                break
        if all_subsets:
            return set(combination)