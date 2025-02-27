def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    length_range = range(115, 135)
    palindromes = {palindrome for length in length_range for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) and palindrome == palindrome[::-1] and palindrome.isalpha()}
    return palindromes