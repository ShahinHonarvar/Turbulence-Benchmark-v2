def palindrome_of_length_n(input):
    ret = set()
    length = 223
    lower_input = input.lower()
    for i in range(len(lower_input) - length + 1):
        substring = lower_input[i:i + length]
        if substring == substring[::-1]:
            ret.add(substring)
    return ret