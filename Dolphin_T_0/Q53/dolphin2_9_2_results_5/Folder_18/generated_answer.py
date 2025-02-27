def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 61):
        candidate = s[i:i + 62]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes