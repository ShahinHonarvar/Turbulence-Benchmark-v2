def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    length = 15
    for y in range(len(input_string) - length + 1):
        for x in range(y, y + length):
            if input_string[x] not in 'abcdefghijklmnopqrstuvwxyz':
                break
        else:
            substring = input_string[y:y + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes