def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s.lower() != s.lower()[::-1]:
        return False
    else:
        return True

def palindrome_of_length_n(s, n):
    palindromes = set()
    for i in range(len(s) - n + 1):
        if n % 2 == 0:
            substr = s[i:i + n]
            if is_palindrome(substr):
                palindromes.add(substr)
        else:
            left_substr = s[i:i + n // 2]
            right_substr = s[i + n // 2 + 1:i + n + 1]
            if is_palindrome(left_substr) and is_palindrome(right_substr[::-1]):
                palindromes.add(s[i:i + n])
    return palindromes