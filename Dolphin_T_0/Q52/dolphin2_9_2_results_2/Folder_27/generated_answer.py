def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    n = 56
    result = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result