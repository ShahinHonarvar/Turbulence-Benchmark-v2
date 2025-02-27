def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 87
    s = s.lower()
    for i in range(len(s) - n + 1):
        candidate = s[i:i + n]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes