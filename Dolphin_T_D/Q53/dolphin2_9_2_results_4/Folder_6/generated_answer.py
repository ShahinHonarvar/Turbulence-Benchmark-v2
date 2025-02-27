def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string_length = len(string)
    palindrome_set = set()
    for i in range(string_length - 21):
        for j in range(i + 2, string_length + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindrome_set.add(sub_string)
    return palindrome_set