def palindrome_of_length_at_least_n(s):
    results = set()
    for i in range(len(s)):
        for j in range(i + 38, len(s) + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                results.add(palindrome)
    return results