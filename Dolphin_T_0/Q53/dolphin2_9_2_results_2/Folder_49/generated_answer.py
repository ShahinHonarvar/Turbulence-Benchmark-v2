def palindrome_of_length_at_least_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 72):
        for j in range(i + 73, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                result.add(sub_string)
    return result