def palindromes_of_specific_lengths(s):
    s = s[22:96]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindrome_set = set()
    for length in range(52, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set