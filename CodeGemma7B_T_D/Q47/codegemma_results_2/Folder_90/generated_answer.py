def palindromes_of_specific_lengths(given_string):
    set_of_palindromes = set()
    for i in range(106, 280):
        for j in range(i, 280):
            if j - i + 1 >= 136 and j - i + 1 <= 151:
                palindrome = given_string[i:j + 1]
                reversed_palindrome = palindrome[::-1].lower()
                if palindrome.lower() == reversed_palindrome:
                    set_of_palindromes.add(palindrome)
    return set_of_palindromes