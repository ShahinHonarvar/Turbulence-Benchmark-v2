def palindromes_of_specific_lengths(input_string):
    input_string = input_string.lower()
    specified_substring = input_string[24:85]
    palindromes = set()
    for length in range(21, 32):
        for i in range(len(specified_substring) - length + 1):
            potential_palindrome = specified_substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes