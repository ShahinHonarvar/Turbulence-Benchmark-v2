def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    input_set = set(input_string.lower())
    valid_input_chars = input_set.intersection(english_letters)
    palindrome_set = set()
    for length in range(136, 161):
        for start in range(100, 296 - length):
            if valid_input_chars.issubset(input_string[start:start + length]):
                if input_string[start:start + length] == input_string[start:start + length][::-1]:
                    palindrome_set.add(input_string[start:start + length])
    return palindrome_set