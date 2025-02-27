def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(75, 96):
        for j in range(7, 10):
            palindrome = s[i:i + j].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result