def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for i in range(12, 93):
        for j in range(42, 78):
            if i + j - 1 <= 92:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindrome_set.add(substring)
    return palindrome_set