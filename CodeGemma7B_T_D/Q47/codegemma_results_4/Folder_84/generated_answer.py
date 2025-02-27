def palindromes_of_specific_lengths(s):
    low, high = (23, 77)
    res = set()
    for i in range(low, high + 1):
        for j in range(i + 13, high + 1):
            palindrome = s[i:j].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                res.add(palindrome)
    return res