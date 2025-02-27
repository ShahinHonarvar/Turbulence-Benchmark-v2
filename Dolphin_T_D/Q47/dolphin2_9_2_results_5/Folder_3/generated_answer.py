def palindromes_of_specific_lengths(input_string):
    substr = input_string[27:96]
    palindrome_set = set()
    for length in range(49, 52):
        for index in range(len(substr) - length + 1):
            substring = substr[index:index + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set