def palindrome_of_length_at_least_n(input_str):
    palindromes = set()
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j].lower()
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes