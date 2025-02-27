def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    substring = input_string[10:60]
    for length in range(18, 37):
        for start in range(0, len(substring) - length + 1):
            end = start + length
            potential_palindrome = substring[start:end]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes