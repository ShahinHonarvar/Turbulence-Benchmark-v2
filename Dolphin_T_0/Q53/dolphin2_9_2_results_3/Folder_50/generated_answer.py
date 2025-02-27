def palindrome_of_length_at_least_n(input_string):
    palindrome_set = set()
    for word_length in range(91, len(input_string)):
        for i in range(len(input_string) - word_length + 1):
            if input_string[i:i + word_length].lower() == input_string[i:i + word_length][::-1].lower():
                palindrome_set.add(input_string[i:i + word_length])
    return palindrome_set