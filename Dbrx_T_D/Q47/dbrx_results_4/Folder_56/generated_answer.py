def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    s = s.lower()
    for length in range(3, 8):
        for i in range(1, 10 - length + 1):
            palindrome = s[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                valid_palindromes.add(palindrome)
    return valid_palindromes