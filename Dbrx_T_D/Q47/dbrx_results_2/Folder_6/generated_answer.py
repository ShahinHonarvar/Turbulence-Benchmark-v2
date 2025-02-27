def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(45, 99):
        for j in range(40, 48):
            if i + j - 1 <= 98:
                palindrome = s[i:i + j].lower()
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    result.add(palindrome)
    return result