def palindromes_of_specific_lengths(s):
    s = s[155:284]
    palindromes = set()
    for length in range(104, 121):
        for start in range(0, len(s) - length + 1):
            palindrome = s[start:start + length]
            palindrome = ''.join(filter(str.isalpha, palindrome)).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes