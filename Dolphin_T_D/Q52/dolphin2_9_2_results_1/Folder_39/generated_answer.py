def palindrome_of_length_n(s):
    s_lower = s.lower()
    length = 59
    palindromes = set()
    for i in range(len(s_lower) - length + 1):
        if s_lower[i:i + length] == s_lower[i:i + length][::-1]:
            palindromes.add(s_lower[i:i + length])
    return palindromes