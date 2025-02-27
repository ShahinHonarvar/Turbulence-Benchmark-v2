def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 87):
        candidate = s[i:i + 88]
        if candidate == candidate[::-1]:
            if candidate.isalpha():
                palindromes.add(candidate)
    return palindromes