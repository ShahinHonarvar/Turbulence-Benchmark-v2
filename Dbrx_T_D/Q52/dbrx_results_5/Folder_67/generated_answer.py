def palindrome_of_length_n(s):
    valid_palindromes = set()
    s = s.lower()
    if len(s) < 42:
        return valid_palindromes
    for i in range(len(s) - 41):
        palindrome = s[i:i + 42]
        if palindrome.isalnum() and palindrome == palindrome[::-1]:
            valid_palindromes.add(palindrome)
    return valid_palindromes