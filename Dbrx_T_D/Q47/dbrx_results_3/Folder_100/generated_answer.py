def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(29, 97):
        for length in range(12, 19):
            if i + length <= len(input_string):
                substring = input_string[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set