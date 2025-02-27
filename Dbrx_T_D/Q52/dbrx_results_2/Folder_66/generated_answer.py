def palindrome_of_length_n(s):
    n = 25
    palindromes = set()
    for i in range(len(s) - n + 1):
        candidate = s[i:i + n]
        if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes