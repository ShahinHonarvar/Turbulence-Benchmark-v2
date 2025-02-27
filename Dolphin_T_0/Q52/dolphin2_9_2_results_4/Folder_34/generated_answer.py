def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 32):
        candidate = s[i:i + 33]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes