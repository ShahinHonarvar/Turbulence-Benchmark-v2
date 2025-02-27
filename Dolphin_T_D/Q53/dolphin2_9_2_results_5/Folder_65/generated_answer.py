def palindrome_of_length_at_least_n(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    lower_input_string = input_string.lower()
    palindromes = set()
    for length in range(15, len(input_string) + 1):
        for i in range(0, len(input_string) - length + 1):
            fragment = lower_input_string[i:i + length]
            if all((letter in english_letters for letter in fragment)) and fragment == fragment[::-1]:
                palindromes.add(fragment)
    return palindromes