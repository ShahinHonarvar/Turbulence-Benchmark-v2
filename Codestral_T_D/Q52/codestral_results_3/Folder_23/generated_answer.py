def palindrome_of_length_n(s):
    palindromes = set()
    n = 69
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes