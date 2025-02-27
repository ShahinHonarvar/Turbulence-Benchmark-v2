def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    len_s = len(s_lower)
    palindromes = set()
    for i in range(len_s):
        for j in range(i + 83, len_s):
            substring = s_lower[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes