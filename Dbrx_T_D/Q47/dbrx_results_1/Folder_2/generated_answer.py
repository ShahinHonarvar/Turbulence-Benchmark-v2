def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(10, 60):
        for length in range(18, 37):
            if i + length - 1 > 50:
                break
            palindrome = s[i - 1:i + length - 1].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result