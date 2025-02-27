def palindrome_of_length_at_least_n(s):
    n = len(s)
    palindrome_set = set()
    for k in range(n):
        for i in range(n - k):
            palindrome = s[i:i + k + 1]
            palindrome = palindrome.lower()
            if palindrome == palindrome[::-1] and len(palindrome) >= 60:
                palindrome_set.add(palindrome)
    return palindrome_set