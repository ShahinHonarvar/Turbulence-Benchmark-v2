def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(65, 100):
        for j in range(26, 34):
            if i + j - 1 < len(s):
                palindrome = s[i:i + j].lower()
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    result.add(palindrome)
    return result