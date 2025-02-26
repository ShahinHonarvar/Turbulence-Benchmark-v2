def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    s = s.lower()
    for start in range(51):
        for length in range(50, 101):
            end = start + length
            if end > 51:
                break
            substring = s[start:end]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set