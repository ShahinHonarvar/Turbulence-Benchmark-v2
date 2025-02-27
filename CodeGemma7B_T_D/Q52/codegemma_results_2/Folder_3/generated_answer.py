def palindrome_of_length_n(word):
    result = set()
    for i in range(len(word) - 99):
        for j in range(i + 1, len(word) - 98 + 1):
            if word[i:j + 1] == word[j:i:-1]:
                result.add(word[i:j + 1].lower())
    return result