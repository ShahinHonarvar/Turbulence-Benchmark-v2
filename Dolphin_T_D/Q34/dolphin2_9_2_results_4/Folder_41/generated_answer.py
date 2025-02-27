def find_original_set(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20):
    s_union = S1
    for i in range(2, 21):
        s_union = s_union.union(eval(f'S{i}'))
    return s_union