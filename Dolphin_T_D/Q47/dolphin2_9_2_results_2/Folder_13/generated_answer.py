def palindromes_of_specific_lengths(input_string):
    inner_substring = input_string[13:96]
    palindrome_set = set()
    for length in range(57, 61):
        for start_index in range(0, len(inner_substring) - length + 1):
            potential_palindrome = inner_substring[start_index:start_index + length]
            lower_case_palindrome = potential_palindrome.lower()
            if lower_case_palindrome == lower_case_palindrome[::-1]:
                if all((x.isalpha() for x in potential_palindrome)):
                    palindrome_set.add(potential_palindrome)
    return palindrome_set