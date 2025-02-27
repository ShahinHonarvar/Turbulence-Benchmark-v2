def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    length = len(input_string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 138, length + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes