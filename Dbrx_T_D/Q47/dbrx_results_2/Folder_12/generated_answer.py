def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(18, 22):
        for start_index in range(62, 89):
            if start_index + length - 1 <= 88:
                potential_palindrome = input_string[start_index:start_index + length]
                if potential_palindrome.lower().isalpha() and set(potential_palindrome).issubset(english_letters):
                    if potential_palindrome == potential_palindrome[::-1]:
                        palindromes.add(potential_palindrome)
    return palindromes