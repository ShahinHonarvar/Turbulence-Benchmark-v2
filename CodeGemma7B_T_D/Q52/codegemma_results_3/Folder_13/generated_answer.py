def palindrome_of_length_n(str):
    n = 206
    palindrome = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            word = str[i:j + 1]
            if len(word) > 1:
                new_word = word.lower()
                if new_word == new_word[::-1]:
                    palindrome.add(word)
    return palindrome