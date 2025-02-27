def palindromes_of_specific_lengths(s):
    substr = s[63:71].lower()
    palindromes = {palindrome for length in range(4, 6) for palindrome in substr if palindrome[:length] == palindrome[-length:][::-1] and palindrome.replace(' ', '').isalpha()}
    return palindromes