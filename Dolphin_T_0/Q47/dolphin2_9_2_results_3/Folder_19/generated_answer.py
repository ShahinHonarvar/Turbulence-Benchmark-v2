def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()
    palindromes = set()
    for len_p in range(3, 8):
        for i in range(len(s) - len_p + 1):
            string_slice = s[i:i + len_p]
            if string_slice == string_slice[::-1]:
                palindromes.add(string_slice)
    return palindromes