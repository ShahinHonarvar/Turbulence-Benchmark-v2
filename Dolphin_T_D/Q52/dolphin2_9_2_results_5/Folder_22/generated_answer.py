def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindrome_set = set()
    for i in range(len(input_string) - 21 + 1):
        substring = input_string[i:i + 20]
        if set(substring).issubset(english_letters):
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set