def all_substring_of_size_n(strv):
    st = set()
    n = 30
    for i in range(len(strv) - n + 1):
        substring = strv[i:i + n]
        st.add(substring)
    return list(st)