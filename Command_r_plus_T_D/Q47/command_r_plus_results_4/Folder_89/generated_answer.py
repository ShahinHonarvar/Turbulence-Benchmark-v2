def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[17:89].lower()
    for length in range(12, 15):
        for start_index in range(len(substring) - length + 1):
            end_index = start_index + length
            potential_palindrome = substring[start_index:end_index]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes