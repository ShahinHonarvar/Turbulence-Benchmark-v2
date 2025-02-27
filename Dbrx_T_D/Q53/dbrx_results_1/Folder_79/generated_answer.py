def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(input_string) - 16):
        for j in range(17, min(58, len(input_string) - i + 1)):
            substring = input_string[i:i + j].lower()
            if substring.translate(str.maketrans('', '', '0123456789')) == substring and set(substring) <= english_letters and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes