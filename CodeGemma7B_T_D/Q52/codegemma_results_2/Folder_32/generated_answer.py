def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 102):
        for j in range(i + 113, len(string)):
            word = string[i:j + 1]
            if word == word[::-1]:
                result.add(word)
    return result