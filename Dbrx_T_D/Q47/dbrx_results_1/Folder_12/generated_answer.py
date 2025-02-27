def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for length in range(18, 22):
        for index in range(62, 89):
            substring = input_string[index:index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set