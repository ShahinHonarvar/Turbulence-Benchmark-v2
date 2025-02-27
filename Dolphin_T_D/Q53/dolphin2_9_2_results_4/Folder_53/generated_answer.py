def palindrome_of_length_at_least_n(string):
    results = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 64, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                results.add(substring)
    return results