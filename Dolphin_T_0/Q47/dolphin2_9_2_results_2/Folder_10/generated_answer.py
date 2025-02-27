def palindromes_of_specific_lengths(test_string):
    specific_substring = test_string[15:61]
    palindrome_set = set()
    for length in range(16, 40):
        for i in range(len(specific_substring) - length + 1):
            substring = specific_substring[i:i + length]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindrome_set.add(substring.lower())
    return palindrome_set