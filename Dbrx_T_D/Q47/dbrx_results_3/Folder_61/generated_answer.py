def palindromes_of_specific_lengths(s):
    s = s.upper()
    return {palindrome for length in range(20, 31) for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]).lower() == palindrome.lower()[::-1] and palindrome.isalpha() and (i <= 30)}