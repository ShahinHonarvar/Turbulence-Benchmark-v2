def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    st = set()
    for i in range(len(s) - 88):
        if len(set(s[i:i + 89])) == 89:
            st.add(s[i:i + 89])
    return list(st)