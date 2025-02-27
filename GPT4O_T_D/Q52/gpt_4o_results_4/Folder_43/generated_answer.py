def palindrome_of_length_n(s):
    n = 51
    palindromes = set()
    s_lower = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s_lower) - n + 1):
        substring = s_lower[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes