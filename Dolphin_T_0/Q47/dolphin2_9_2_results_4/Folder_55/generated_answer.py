def palindromes_of_specific_lengths(s):
    s = s[9:76]
    palindrome_set = set()
    for length in range(10, 21):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindrome_set.add(''.join(filter(str.isalpha, substring)))
    return palindrome_set