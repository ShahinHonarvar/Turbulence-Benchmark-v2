def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(119, 256):
        for l in range(104, 124):
            for j in range(i - l + 1):
                if s[i - j] == s[i + j + 1]:
                    palindrome = s[i - j:i + j + 2].lower()
                    if palindrome.isalpha():
                        palindromes.add(palindrome)
    return palindromes