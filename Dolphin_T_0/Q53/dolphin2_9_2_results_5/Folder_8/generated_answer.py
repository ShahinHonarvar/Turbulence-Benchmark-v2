def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 44):
        for j in range(i + 45, len(s_lower) + 1):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes