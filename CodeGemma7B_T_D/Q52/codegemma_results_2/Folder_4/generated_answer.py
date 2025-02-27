def palindrome_of_length_n(s):
    low_s = s.lower()
    palindromes = set()
    for i in range(len(low_s) - 14):
        for j in range(i + 15):
            if low_s[i:j] == low_s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes