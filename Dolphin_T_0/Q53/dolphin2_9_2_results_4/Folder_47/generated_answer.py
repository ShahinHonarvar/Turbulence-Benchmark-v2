def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = 77
    output = set()
    for i in range(len(string)):
        for j in range(i + length, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                output.add(sub_string)
    return output