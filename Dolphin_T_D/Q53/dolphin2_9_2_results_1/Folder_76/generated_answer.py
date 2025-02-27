def palindrome_of_length_at_least_n(input_str):
    input_str = input_str.lower()
    result = set()
    for i in range(len(input_str)):
        for j in range(i + 137, len(input_str) + 1):
            sub_string = input_str[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                result.add(sub_string)
    return result