def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        if i + 115 > len(s):
            continue
        for j in range(i + 1, min(len(s) + 1, i + 116)):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result