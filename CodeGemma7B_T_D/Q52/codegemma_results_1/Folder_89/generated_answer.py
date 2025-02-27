def palindrome_of_length_n(string):
    result = set()
    lowercase_string = string.lower()
    for i in range(len(lowercase_string) - 36):
        for j in range(i + 37, len(lowercase_string) + 1):
            if lowercase_string[i:j] == lowercase_string[j - 37:j][::-1]:
                result.add(string[i:j])
    return result