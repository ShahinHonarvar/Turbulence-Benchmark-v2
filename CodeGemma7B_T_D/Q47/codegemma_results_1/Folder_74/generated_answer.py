def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(30, 85):
        for j in range(i - 11, i + 1):
            palindrome = s[j:i + 1]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result