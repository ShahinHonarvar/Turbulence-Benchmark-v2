def palindromes_of_specific_lengths(input_string):
    internal_string = input_string[100:292]
    palindrome_set = set()
    for length in range(154, 183):
        for i in range(len(internal_string) - length + 1):
            substring = internal_string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set