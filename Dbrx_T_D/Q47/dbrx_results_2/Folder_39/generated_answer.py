def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(50, 54):
        for index in range(31, 92 - length):
            palindrome = s[index:index + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result