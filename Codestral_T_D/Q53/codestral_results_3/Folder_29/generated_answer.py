def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(78, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes