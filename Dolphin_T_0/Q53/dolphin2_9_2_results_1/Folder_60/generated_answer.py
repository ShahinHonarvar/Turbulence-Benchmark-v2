def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 80
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes