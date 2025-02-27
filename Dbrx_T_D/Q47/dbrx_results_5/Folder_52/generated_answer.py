def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for length in range(13, 43):
        for index in range(44, 100 - length + 1):
            potential_palindrome = input_string[index:index + length].lower()
            if potential_palindrome == potential_palindrome[::-1]:
                palindrome_set.add(potential_palindrome)
    return palindrome_set