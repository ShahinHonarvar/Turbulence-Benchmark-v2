def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34):
    result = set()
    for i in range(1, 35):
        for j in range(1, 35):
            for k in range(1, 35):
                for l in range(1, 35):
                    result.add(i * j * k * l)
    return result.union(s1).union(s2).union(s3).union(s4).union(s5).union(s6).union(s7).union(s8).union(s9).union(s10).union(s11).union(s12).union(s13).union(s14).union(s15).union(s16).union(s17).union(s18).union(s19).union(s20).union(s21).union(s22).union(s23).union(s24).union(s25).union(s26).union(s27).union(s28).union(s29).union(s30).union(s31).union(s32).union(s33).union(s34)