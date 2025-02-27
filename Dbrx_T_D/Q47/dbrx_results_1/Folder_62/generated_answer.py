import string

def palindromes_of_specific_lengths(input_string):
    english_letters = string.ascii_letters
    palindromes = set()
    for length in range(52, 57):
        for start_index in range(26, len(input_string) - length + 1):
            if input_string[start_index:start_index + length].lower().isalpha():
                substring = input_string[start_index:start_index + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes