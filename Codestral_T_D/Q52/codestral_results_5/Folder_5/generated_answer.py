def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 16):
        sub = s[i:i + 17]
        if sub.lower() == sub.lower()[::-1]:
            palindromes.add(sub)
    return palindromes