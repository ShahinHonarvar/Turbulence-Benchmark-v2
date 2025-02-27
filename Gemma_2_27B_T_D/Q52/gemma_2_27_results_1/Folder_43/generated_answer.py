def palindrome_of_length_n(input_string):
    palindromes = set()
    for i in range(len(input_string) - 50):
        substring = input_string[i:i + 51].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes