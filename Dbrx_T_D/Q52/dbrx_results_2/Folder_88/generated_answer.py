def palindrome_of_length_n(s):
    pallet = set()
    for i in range(len(s) - 12):
        sub_s = s[i:i + 13].lower()
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            pallet.add(sub_s)
    return pallet