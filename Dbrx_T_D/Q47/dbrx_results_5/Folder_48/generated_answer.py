def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    return {palindrome for length in range(104, 121) for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) == palindrome[::-1] and palindrome.isalpha()}