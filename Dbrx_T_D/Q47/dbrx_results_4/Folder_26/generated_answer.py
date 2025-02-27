def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(24, 85):
        for length in range(21, 32):
            if i + length <= len(input_string):
                potential_palindrome = input_string[i:i + length].lower()
                if potential_palindrome == potential_palindrome[::-1]:
                    palindromes.add(potential_palindrome)
    return palindromes