def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 77):
        for j in range(i + 78, len(string) + 1):
            if string[i:j] == string[i:j][::-1]:
                result.add(string[i:j])
    return result