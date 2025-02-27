def palindrome_of_length_n(s):
    n = 54
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - n + 1):
        substring = s_lower[i:i + n].strip()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes