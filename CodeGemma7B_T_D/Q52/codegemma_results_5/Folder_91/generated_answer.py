def palindrome_of_length_n(st):
    st = st.lower()
    res = set()
    for i in range(len(st) - 6):
        temp = st[i:i + 7]
        if temp == temp[::-1]:
            res.add(temp)
    return res