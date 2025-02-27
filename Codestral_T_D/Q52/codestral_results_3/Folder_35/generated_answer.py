def palindrome_of_length_n(s):
    n = 116
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.lower() == sub.lower()[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes