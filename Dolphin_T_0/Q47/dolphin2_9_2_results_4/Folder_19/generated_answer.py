def palindromes_of_specific_lengths(s):
    subs = s[9:56].lower()
    sub_palindromes = set()
    for length in range(3, 8):
        for i in range(len(subs) - length + 1):
            st = subs[i:i + length]
            if st == st[::-1] and st.isalpha():
                sub_palindromes.add(st)
    return sub_palindromes