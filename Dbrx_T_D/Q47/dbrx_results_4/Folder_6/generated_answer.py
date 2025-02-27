def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    palindromes = {palindrome for length in range(40, 48) for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) == palindrome[::-1]}
    return palindromes