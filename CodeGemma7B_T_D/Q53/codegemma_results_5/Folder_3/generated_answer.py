def palindrome_of_length_at_least_n(s):
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 59, n):
            palindrome = s[i:j + 1]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result