def find_original_set(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19):
    set = a1.copy()
    for i in range(2, 20):
        for arg in locals()['a' + str(i)]:
            set.add(arg)
    return set