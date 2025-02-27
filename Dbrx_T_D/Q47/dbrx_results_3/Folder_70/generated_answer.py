def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(24, 53):
        for i in range(10, len(s) - length + 1):
            palindrome = s[i:i + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result