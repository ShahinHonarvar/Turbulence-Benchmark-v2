def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    sub = s[13:100].lower()
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(sub) - length + 1):
            potential_palindrome = sub[i:i + length]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes