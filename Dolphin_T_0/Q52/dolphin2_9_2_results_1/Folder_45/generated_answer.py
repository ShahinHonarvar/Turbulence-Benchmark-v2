def palindrome_of_length_n(string):
    result = set()
    lower_string = string.lower()
    for i in range(len(string) - 20):
        if lower_string[i:i + 21] == lower_string[i:i + 21][::-1]:
            result.add(lower_string[i:i + 21])
    return result