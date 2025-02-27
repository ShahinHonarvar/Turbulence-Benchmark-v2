def palindrome_of_length_at_least_n(input_str):
    input_str = input_str.lower()
    palindromes = set()
    for length in range(69, len(input_str) + 1):
        for i in range(0, len(input_str) - length + 1):
            substring = input_str[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes