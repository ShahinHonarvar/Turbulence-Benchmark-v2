def palindrome_of_length_n(word):
    palindrome_set = set()
    word = word.lower()
    for i in range(len(word) - 56):
        for j in range(i + 57, len(word)):
            palindrome = word[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set