def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(13, 100):
        for j in range(26, 30):
            if i + j - 1 <= 99:
                sub_s = s[i:i + j].lower()
                if sub_s == sub_s[::-1] and sub_s.isalpha():
                    palindromes.add(sub_s)
    return palindromes