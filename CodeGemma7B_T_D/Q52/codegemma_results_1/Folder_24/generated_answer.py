def palindrome_of_length_n(word):
    for i in range(len(word) - 28):
        for j in range(i + 1, len(word) - 27 + i):
            if word[i:j + 1][::-1] == word[i:j + 1]:
                return {word[i:j + 1]}
    return set()