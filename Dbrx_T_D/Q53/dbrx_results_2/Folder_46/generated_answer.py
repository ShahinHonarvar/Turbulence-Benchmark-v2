def palindrome_of_length_at_least_n(input_string):
    palindrome_set = set()
    for i in range(len(input_string) - 86 + 1):
        for length in range(86, len(input_string) - i + 1):
            substring = input_string[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set