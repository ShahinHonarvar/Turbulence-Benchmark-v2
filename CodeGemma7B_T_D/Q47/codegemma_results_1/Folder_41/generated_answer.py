def palindromes_of_specific_lengths(s):
    lower_cased = s.lower()
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 2, 8):
            palindrome = lower_cased[i:j]
            if palindrome == palindrome[::-1] and 3 <= len(palindrome) <= 4:
                palindromes.add(palindrome)
    return palindromes