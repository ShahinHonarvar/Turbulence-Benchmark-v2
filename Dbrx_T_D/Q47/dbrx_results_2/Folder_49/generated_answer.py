def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(10, 51):
        for i in range(10, 101 - length):
            palindrome = s[i:i + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                valid_palindromes.add(palindrome)
    return valid_palindromes