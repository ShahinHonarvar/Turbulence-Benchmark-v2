def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string)):
        for j in range(i + 58, len(input_string)):
            substring = input_string[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result