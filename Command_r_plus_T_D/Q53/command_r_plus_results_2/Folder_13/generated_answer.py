def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes