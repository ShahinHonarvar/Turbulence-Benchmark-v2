def all_substring_of_size_n(s):
    n = 39
    st = set()
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if len(set(subs)) == n:
            st.add(subs)
    return list(st)