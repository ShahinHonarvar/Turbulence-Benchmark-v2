def palindrome_of_length_n(s):
    s = s.lower()
    set_res = set()
    for i in range(len(s) - 84):
        subs = s[i:i + 85]
        if subs == subs[::-1] and subs.isalpha():
            set_res.add(subs)
    return set_res