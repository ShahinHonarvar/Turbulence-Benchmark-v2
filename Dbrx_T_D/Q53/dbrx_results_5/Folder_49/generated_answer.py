def palindrome_of_length_at_least_n(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for center_index in range(len(input_string)):
        for radius in range(36):
            if center_index - radius < 0 or center_index + radius > len(input_string):
                break
            if input_string[center_index - radius] not in english_letters or input_string[center_index + radius] not in english_letters:
                break
            if input_string[center_index - radius] != input_string[center_index + radius]:
                break
            if (center_index - radius) % 2 == 0 and (center_index + radius) % 2 == 1:
                continue
            palindrome = input_string[center_index - radius:center_index + radius + 1]
            if len(palindrome) >= 73:
                palindromes.add(palindrome.lower())
    return palindromes