def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = len(string)
    result = set()
    for i in range(length):
        for j in range(i + 149, length):
            sub_string = string[i:j + 1]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                result.add(sub_string)
    return result