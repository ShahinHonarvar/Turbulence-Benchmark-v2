def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if s[i].isalpha() and len(s) - i >= 255:
            possible_palindrome = s[i:i + 255]
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)
    return palindromes