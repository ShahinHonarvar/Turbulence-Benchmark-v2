def palindrome_of_length_at_least_n(word):
    word = word.lower()
    palindrome_list = []
    for i in range(len(word)):
        for j in range(i, len(word)):
            if word[i:j + 1] == word[i:j + 1][::-1] and len(word[i:j + 1]) >= 45:
                palindrome_list.append(word[i:j + 1])
    return set(palindrome_list)