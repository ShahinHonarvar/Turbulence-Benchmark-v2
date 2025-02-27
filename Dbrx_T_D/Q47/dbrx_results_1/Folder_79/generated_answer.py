def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for length in range(3, 5):
        for i in range(1, 9 - length + 1):
            palindrome = s[i:i + length]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result