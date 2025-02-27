def palindrome_of_length_n(words):
    palindrome_set = set()
    for word in words:
        word = word.lower()
        for i in range(len(word) - 20):
            substring = word[i:i + 21]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set