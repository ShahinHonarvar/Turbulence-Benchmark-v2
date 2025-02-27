def palindrome_of_length_n(string):
    palindrome = set()
    for i in range(len(string) - 172):
        for j in range(i + 173):
            word = string[i:j]
            if word == word[::-1]:
                palindrome.add(word.casefold())
    return palindrome