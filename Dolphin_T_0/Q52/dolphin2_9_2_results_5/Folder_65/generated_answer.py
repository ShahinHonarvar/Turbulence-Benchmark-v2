def palindrome_of_length_n(s):
    set_of_palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - 34):
        if s_lower[i:i + 35] == s_lower[i:i + 35][::-1]:
            set_of_palindromes.add(s[i:i + 35])
    return set_of_palindromes