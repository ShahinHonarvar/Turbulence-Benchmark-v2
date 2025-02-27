def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(130, 296):
        for j in range(i + 103, i + 159):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes