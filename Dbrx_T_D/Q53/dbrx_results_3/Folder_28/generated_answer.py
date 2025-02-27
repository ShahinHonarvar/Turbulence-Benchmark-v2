def palindrome_of_length_at_least_n(input_string, min_length=42):
    input_string = ''.join((c.lower() for c in input_string if c.isalpha()))
    palindromes = set()
    for i in range(len(input_string) - min_length + 1):
        for j in range(i + min_length, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes