def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substr = string[i:j + 1]
            if substr == substr[::-1] and len(substr) == 42 and substr.isalpha():
                result.add(substr)
    return result