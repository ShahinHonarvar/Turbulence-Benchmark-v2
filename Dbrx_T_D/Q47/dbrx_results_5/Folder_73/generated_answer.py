def palindromes_of_specific_lengths(s):
    s = s.lower()[21:63]
    palindromes = {palindrome for length in range(22, 34) for i in range(len(s) - length + 1) for palindrome in [s[i:i + length]] if palindrome == palindrome[::-1]}
    return palindromes