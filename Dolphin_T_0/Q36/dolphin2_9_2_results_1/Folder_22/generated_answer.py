def filter_chars(st):
    for ch in range(55, 85):
        if st[ch] > ';' and st[ch] < 'z':
            st = st.replace(st[ch], '')
    return st