def palindrome_of_length_n(str):
    palindrome = set()
    for word in str.lower().split():
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                str = word[i:j + 1]
                if str == str[::-1]:
                    palindrome.add(str)
    return palindrome