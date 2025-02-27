def palindrome_of_length_at_least_n(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    length = len(input_string)
    for i in range(length):
        for j in range(i + 94, length + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes