def find_original_set(s, st=set(), c=0, o=set()):
    if c == 746:
        return o
    for i in s:
        if i in st:
            continue
        st.add(i)
        o = o | s
        if find_original_set(s, st, c + 1, o):
            return o
        st.remove(i)
        o = o - {i}