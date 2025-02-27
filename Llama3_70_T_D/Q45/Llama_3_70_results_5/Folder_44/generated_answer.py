def palindromes_between_indices(s):
    s = s[2:8].lower()
    palindrome_set = set()
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set