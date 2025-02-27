def palindrome_of_length_n(input_str):
    input_str = input_str.lower()
    palindromes = set()
    for i in range(len(input_str)):
        for j in range(i + 38, len(input_str)):
            substring = input_str[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes