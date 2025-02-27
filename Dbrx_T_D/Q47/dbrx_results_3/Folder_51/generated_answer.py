def palindromes_of_specific_lengths(s):
    result = set()
    s = s[2:9].lower()
    for i in range(len(s) - 2):
        for j in [3, 4]:
            if i + j <= len(s):
                palindrome = s[i:i + j]
                if palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result