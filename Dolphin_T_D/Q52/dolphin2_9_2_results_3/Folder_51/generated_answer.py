def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 73, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1] and all((character.isalpha() for character in sub_string)):
                palindromes.add(sub_string)
    return palindromes