def palindromes_of_specific_lengths(s):
    sub_s = s[10:75]
    palindromes = set()
    for i in range(10, 75):
        for length in range(6, 9):
            sub_palindrome = sub_s[i:i + length]
            if sub_palindrome == sub_palindrome[::-1] and sub_palindrome.isalpha() and (sub_palindrome.lower() == sub_palindrome):
                palindromes.add(sub_palindrome)
    return palindromes