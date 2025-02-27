def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i:j + 1].lower() == string[i:j + 1][::-1]:
                result.add(string[i:j + 1])
    return result