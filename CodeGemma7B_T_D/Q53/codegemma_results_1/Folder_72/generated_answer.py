def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if j - i + 1 >= 88 and string[i:j + 1].lower() == string[i:j + 1][::-1].lower():
                result.add(string[i:j + 1])
    return result