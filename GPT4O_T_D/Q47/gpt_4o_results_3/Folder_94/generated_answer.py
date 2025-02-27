def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s[40:95])).lower()
    palindrome_set = set()
    for length in range(45, 52):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set