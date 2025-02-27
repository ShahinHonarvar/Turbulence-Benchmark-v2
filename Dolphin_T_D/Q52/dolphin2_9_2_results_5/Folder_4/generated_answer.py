def palindrome_of_length_n(s):
    s_lower = s.lower()
    n = 15
    palindromes = set()
    for i in range(len(s_lower) - n + 1):
        substring = s_lower[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes