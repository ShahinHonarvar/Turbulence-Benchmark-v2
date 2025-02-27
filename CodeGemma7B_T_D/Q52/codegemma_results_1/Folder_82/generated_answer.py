def palindrome_of_length_n(word):
    palindrome = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) - 27):
            if word[i].lower() == word[j].lower():
                if word[j:j + 28] == word[j:j + 28][::-1]:
                    palindrome.add(word[j:j + 28])
    return palindrome