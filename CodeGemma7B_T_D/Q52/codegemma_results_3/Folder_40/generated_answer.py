def palindrome_of_length_n(string):
    palindrome_set = set()
    for i in range(len(string) - 2):
        word = string[i:i + 3]
        if word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set