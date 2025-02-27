def palindrome_of_length_at_least_n(word):
    palindrome = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i:j + 1] == word[i:j + 1][::-1] and len(word[i:j + 1]) >= 38:
                palindrome.add(word[i:j + 1].lower())
    return palindrome