def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(8):
        for j in range(4, 6):
            if i + j - 1 >= len(s):
                break
            sub_s = s[i:i + j].lower()
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes