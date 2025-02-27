def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 415):
        sub = s[i:i + 416]
        if sub.lower() == sub.lower()[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes