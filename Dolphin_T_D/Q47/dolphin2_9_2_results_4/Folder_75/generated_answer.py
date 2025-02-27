def palindromes_of_specific_lengths(string):
    substring = string[30:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring)):
            found_palindrome = substring[i:i + length]
            if found_palindrome == found_palindrome[::-1] and all((char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for char in found_palindrome)):
                palindromes.add(found_palindrome)
    return palindromes