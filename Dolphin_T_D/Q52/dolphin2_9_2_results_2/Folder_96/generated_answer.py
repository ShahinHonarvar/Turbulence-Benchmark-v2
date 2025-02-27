def palindrome_of_length_n(input_string):
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 83, len(input_string)):
            substring = input_string[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and len(substring) == 83:
                palindromes.add(substring)
    return palindromes