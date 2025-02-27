def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(0, len(s)):
        if len(s[i:]) >= 17:
            potential_palindrome = s[i:i + 17]
            if potential_palindrome == potential_palindrome[::-1]:
                if potential_palindrome.isalpha():
                    palindromes.add(potential_palindrome)
    return palindromes