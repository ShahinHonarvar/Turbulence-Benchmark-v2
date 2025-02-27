def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(12, 93):
        for length in range(42, 78):
            if i + length - 1 < len(s):
                palindrome = s[i:i + length].lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes