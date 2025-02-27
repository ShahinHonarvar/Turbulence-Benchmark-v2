def palindrome_of_length_n(s):
    palindromes = set()
    length = 474
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub.lower() == sub.lower()[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes