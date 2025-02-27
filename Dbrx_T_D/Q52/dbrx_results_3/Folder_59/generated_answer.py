def palindrome_of_length_n(string):
    n = 39
    palindromes = set()
    for i in range(len(string) - n + 1):
        potential_palindrome = string[i:i + n]
        if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and potential_palindrome.isalpha():
            palindromes.add(potential_palindrome)
    return palindromes