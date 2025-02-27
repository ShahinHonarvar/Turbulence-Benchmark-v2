def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(24, 34):
        for i in range(35, len(s) - length + 1):
            palindrome = s[i:i + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                valid_palindromes.add(palindrome)
    return valid_palindromes