def filter_chars(st):
    for i in range(69, 81):
        for c in st:
            if c == st[i]:
                st = st.replace(c, '', max(0, st.count(c) - 1))
    return st