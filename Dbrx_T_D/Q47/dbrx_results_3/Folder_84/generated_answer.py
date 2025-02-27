def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(23, 78):
        for length in range(13, 41):
            substring = input_string[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set